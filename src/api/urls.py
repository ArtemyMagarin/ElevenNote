from django.urls import path, re_path

from rest_framework.authtoken.views import obtain_auth_token

from .views import TagListCreateView, TagRetrieveUpdateDestroyView
from .views import NoteListCreateView, NoteRetrieveUpdateDestroyView
from .views import BookListCreateView, BookRetrieveUpdateDestroyView 
from .views import UserCreateView, UserRetrieveUpdateView, UserListView
from .views import activate


app_name = 'api'


urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='taglist'),
    re_path(r'tag/(?P<pk>\d+)/$', TagRetrieveUpdateDestroyView.as_view(), name="tag"),

    path('notes/', NoteListCreateView.as_view(), name="notelist"),
    re_path(r'note/(?P<pk>\d+)/$', NoteRetrieveUpdateDestroyView.as_view(), name="note"),

    path('books/', BookListCreateView.as_view(), name="booklist"),
    re_path(r'book/(?P<pk>\d+)/$', BookRetrieveUpdateDestroyView.as_view(), name="book"),

    path('user/', UserCreateView.as_view(), name='usercreate'),
    path('user/edit/', UserRetrieveUpdateView.as_view(), name="user"), 
    path('registered-user/', UserListView.as_view(), name="usersearch"),

    re_path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),

    path('api-token-auth/', obtain_auth_token)
]
