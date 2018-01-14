from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    owner = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE, default=1)

    def was_published_recently(self):
        now = timezone.now()
        return now - timezone.timedelta(days=1) <= self.pub_date <= now
        
