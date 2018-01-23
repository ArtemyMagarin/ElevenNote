from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# from tags.models import Tag

# Create your models here.




class Note(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField()
    pub_date = models.DateTimeField('date published')
    owner = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE, default=1)
    tags = models.ManyToManyField('tags.Tag', blank=True)


    def was_published_recently(self):
        now = timezone.now()
        return now - timezone.timedelta(days=1) <= self.pub_date <= now
        

