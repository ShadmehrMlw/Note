from datetime import datetime

from django.db import models


# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=1000)
    body = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title