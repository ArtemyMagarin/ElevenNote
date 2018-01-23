from django.urls import path,re_path

from .views import TagList, TagCreate
from notes.views import NotesByTag
app_name = 'tags'

urlpatterns = [
    path('', TagList.as_view(), name='index'),
    re_path(r'^(?P<tag>[\w_-]+)/$', NotesByTag.as_view(), name='notesByTag'),
    re_path(r'^new/(?P<tag>[\w_-]+)/$', TagCreate.as_view(), name='createTag'),
]