from django.urls import path, re_path

from .views import NoteList, NoteDetail, NoteCreate, NoteUpdate, NoteDelete, NoteSimpleList, NoteAddTag, NoteDeleteTag
app_name = 'notes'

urlpatterns = [
    path('', NoteList.as_view(), name='index'),
    path('notes/', NoteSimpleList.as_view(), name='notelist'),
    path('<int:pk>/', NoteDetail.as_view(), name='detail'),
    path('<int:pk>/edit/', NoteUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', NoteDelete.as_view(), name='delete'),
    path('new/', NoteCreate.as_view(), name='create'),
    re_path(r'(?P<pk>\d+)/(?P<tag>[\w_-]+)/$', NoteAddTag.as_view(), name='addTag'),
    re_path(r'(?P<pk>\d+)/(?P<tag>[\w_-]+)/delete/$', NoteDeleteTag.as_view(), name='deleteTag'),
]