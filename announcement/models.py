from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from sheets.models import Sheet


class Announcement(models.Model):
    title = models.CharField(max_length=5000, default='', blank=True)
    content = models.CharField(max_length=5000, default='', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)
    sheets = models.ForeignKey(Sheet, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
