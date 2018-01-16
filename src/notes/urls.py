from django.urls import path

from .views import NoteList, NoteDetail, NoteCreate, NoteUpdate, NoteDelete, NoteSimpleList
app_name = 'notes'

urlpatterns = [
    path('', NoteList.as_view(), name='index'),
    path('notes/', NoteSimpleList.as_view(), name='notelist'),
    path('<int:pk>/', NoteDetail.as_view(), name='detail'),
    path('<int:pk>/edit/', NoteUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', NoteDelete.as_view(), name='delete'),
    path('new/', NoteCreate.as_view(), name='create'),
]