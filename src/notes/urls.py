from django.urls import path, re_path, register_converter

from .views import NoteList, NoteDetail, NoteCreate, NoteUpdate, NoteDelete, NoteSimpleList, NoteAddTag, NoteDeleteTag, NoteSearch
app_name = 'notes'

from .converters import QueryConverter

register_converter(QueryConverter, 'q')


urlpatterns = [
    path('', NoteList.as_view(), name='index'),
    path('notes/', NoteSimpleList.as_view(), name='notelist'),
    path('<int:pk>/', NoteDetail.as_view(), name='detail'),
    path('<int:pk>/edit/', NoteUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', NoteDelete.as_view(), name='delete'),
    path('new/', NoteCreate.as_view(), name='create'),
    re_path(r'(?P<pk>\d+)/(?P<tag>[\w_-]+)/$', NoteAddTag.as_view(), name='addTag'),
    re_path(r'(?P<pk>\d+)/(?P<tag>[\w_-]+)/delete/$', NoteDeleteTag.as_view(), name='deleteTag'),
    re_path(r'search/(?P<q>[\w\d%-_ ]+)/$', NoteSearch.as_view(), name='search'),
]