from django.db import models
import json
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Posts(models.Model):
    username = models.TextField()
    post = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)