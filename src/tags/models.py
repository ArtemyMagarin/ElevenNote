from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
	body = models.CharField(max_length=30)
	owner = models.ForeignKey(User, related_name='tags', on_delete=models.CASCADE, default=1)

	