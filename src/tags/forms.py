from django import forms

from .models import Tag

class TagCreateForm(forms.ModelForm):
    body = forms.CharField()

    class Meta:
        model = Tag
        fields = ['body']

