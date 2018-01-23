from django import forms

from ckeditor.fields import RichTextFormField

from .models import Note

class NoteForm(forms.ModelForm):
    title = forms.CharField()
    body = RichTextFormField()

    class Meta:
        model = Note
        fields = ['title', 'body']

