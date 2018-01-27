from django.db import models
from django.utils import timezone
from accounts.models import User
from ckeditor.fields import RichTextField


class Tag(models.Model):
    body = models.CharField(max_length=30)
    owner = models.ForeignKey(User, related_name='tags', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return '%s' % (self.body)

class Book(models.Model):
    owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE, default=1)
    viewers = models.ManyToManyField(User, related_name='book_viewers', blank=True)
    editors = models.ManyToManyField(User, related_name='book_editors', blank=True)

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % (self.title)

    def get_viewers(self):
        return ", ".join([v.email for v in self.viewers.all()])

    def get_editors(self):
        return ", ".join([e.email for e in self.editors.all()])


class Note(models.Model):
    owner = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE, default=1)
    viewers = models.ManyToManyField(User, related_name='note_viewers', blank=True)
    editors = models.ManyToManyField(User, related_name='note_editors', blank=True)
    last_editor = models.ForeignKey(User, related_name='note_last_editor', on_delete=models.CASCADE, default=1)
    
    book = models.ForeignKey(Book, related_name="notes", on_delete=models.CASCADE, default=1)
    tags = models.ManyToManyField(Tag, blank=True)

    title = models.CharField(max_length=200)
    body = RichTextField()
    pub_date = models.DateTimeField('date published')


    class Meta:
        ordering = ('pub_date', )

    def __str__(self):
        return '%s' % (self.title)

    def was_published_recently(self):
        now = timezone.now()
        return now - timezone.timedelta(days=1) <= self.pub_date <= now

    def get_viewers(self):
        return ", ".join([v.email for v in self.viewers.all()])

    def get_editors(self):
        return ", ".join([e.email for e in self.editors.all()])


