from django.utils import timezone
from django.http import JsonResponse

from rest_framework.exceptions import PermissionDenied, MethodNotAllowed
from rest_framework.permissions import IsAuthenticated
from .permissions import IsActive
from rest_framework import generics

from .serializers import TagSerializer, NoteSerializer, BookSerializer, UserSerializer
from notes.models import Tag, Note, Book
from accounts.models import User

from django.db.models import Q

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.core.mail import EmailMessage

class TagListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsActive)
    serializer_class = TagSerializer

    def get_queryset(self):
        return Tag.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsActive)
    serializer_class = TagSerializer

    def get_queryset(self):
        queryset = Tag.objects.filter(pk=self.kwargs.get('pk', None))       
        return queryset

    def perform_update(self, serializer):
        tag = self.get_object()

        if tag.owner != self.request.user:
            raise PermissionDenied()

        serializer.save()


    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied()
        instance.delete()


class NoteListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsActive)
    serializer_class = NoteSerializer

    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title', 'body', 'tags__body')


    def get_queryset(self):
        queryset = Note.objects.filter(Q(owner=self.request.user) | Q(editors=self.request.user) | Q(viewers=self.request.user)).distinct()
        return queryset

    def perform_create(self, serializer):
        book = Book.objects.get(pk=self.request.POST['book'])

        if book.owner != self.request.user and self.request.user not in book.editors.all():
            raise PermissionDenied()

        serializer.save(owner=self.request.user, pub_date=timezone.now(), last_editor=self.request.user)


class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsActive)
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = Note.objects.filter(Q(pk=self.kwargs.get('pk', None)), Q(owner=self.request.user) | Q(editors=self.request.user) | Q(viewers=self.request.user)).distinct()
        return queryset

    def perform_update(self, serializer):
        note = self.get_object()

        # if not owner or editor
        if note.owner != self.request.user and self.request.user not in note.editors.all():
            raise PermissionDenied()

        # if not owner is trying change the book 
        if int(note.book.id) != int(self.request.POST['book']):
            if note.owner != self.request.user:
                raise PermissionDenied(detail='Only the creator of a note can change the book')

        # if owner is trying add another's book
        if note.owner != Book.objects.get(pk=self.request.POST['book']).owner:
            raise PermissionDenied(detail='You can add notes only to your own books')

        serializer.save(pub_date=timezone.now(), last_editor=self.request.user)


    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied()
        instance.delete()



class BookListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsActive)
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsActive)
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.filter(Q(pk=self.kwargs.get('pk', None)), Q(owner=self.request.user) | Q(editors=self.request.user) | Q(viewers=self.request.user)).distinct()
        return queryset

    def perform_update(self, serializer):
        book = self.get_object()
        if book.owner != self.request.user and self.request.user not in book.editors.all():
            raise PermissionDenied()

        serializer.save()


    def perform_destroy(self, instance):
        
        if instance.owner != self.request.user:
            raise PermissionDenied()
        instance.delete()


class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsActive)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('email', 'id')


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            raise MethodNotAllowed("create new user", detail="You already have an account")
        user = serializer.save()

        current_site = get_current_site(self.request)
        mail_subject = 'Activate your ElevenNote account.'

        uid = str(urlsafe_base64_encode(force_bytes(user.pk)))[2:-1]
        token = account_activation_token.make_token(user)

        message = f'Hi {user.email},\nPlease click on the link to confirm your registration,\nhttp://{current_site.domain}/api/activate/{uid}/{token}/'
        to_email = user.email
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()

        return JsonResponse({'detail': 'Please confirm your email address to complete the registration'})

class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, IsActive)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def perform_update(self, serializer):
        user = self.get_object()
        if user != self.request.user:
            raise PermissionDenied()

        instanse = serializer.save()
        instanse.set_password(instanse.password)
        instanse.save()


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        print(uid)
        user = User.objects.get(pk=uid)
        print(user.email)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return JsonResponse({'detail': 'Thank you for your email confirmation. Now you can login your account.'})
    else:
        return JsonResponse({'detail': 'Activation link is invalid!'})