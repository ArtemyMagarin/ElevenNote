from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.core.exceptions import PermissionDenied

from .models import Note
from .forms import NoteForm
from .mixins import NoteMixin

class NoteList(LoginRequiredMixin, NoteMixin, ListView):
    template_name = 'note/index.html'
    context_object_name = 'latest_note_list'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoteList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user).order_by('-pub_date')


class NoteSimpleList(LoginRequiredMixin, NoteMixin, ListView):
    template_name = 'note/note_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoteSimpleList, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user).order_by('-pub_date')



class NoteDetail(LoginRequiredMixin, NoteMixin, DetailView):
    model = Note
    template_name = 'note/detail.html'
    context_object_name = 'note'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoteDetail, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.owner != self.request.user:
            raise PermissionDenied

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class NoteCreate(LoginRequiredMixin, NoteMixin, CreateView):
    form_class = NoteForm
    template_name = 'note/create.html'
    success_url = reverse_lazy('notes:index')

    def get_success_url(self):
        return reverse('notes:detail', kwargs={
            'pk': self.object.pk
        })

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.pub_date = timezone.now()
        return super(NoteCreate, self).form_valid(form)


class NoteUpdate(LoginRequiredMixin, NoteMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note/edit.html'

    def get_success_url(self):
        return reverse('notes:detail', kwargs={
            'pk': self.object.pk
        })

    def form_valid(self, form):
        form.instance.pub_date = timezone.now()
        return super(NoteUpdate, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.check_user_or_403(self.object.owner)
        return super(NoteUpdate, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.check_user_or_403(self.object.owner)
        return super(NoteUpdate, self).post(request, *args, **kwargs)


class NoteDelete(LoginRequiredMixin, NoteMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notes:index')
    # def get_success_url(self):
    #     return reverse('notes:update', kwargs={
    #         'pk': self.object.pk
    #     })

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.check_user_or_403(self.object.owner)
        return super(NoteDelete, self).post(request, *args, **kwargs)

