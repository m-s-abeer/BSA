from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.

class Badge(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    image = models.ImageField(default='badges_pics/default.jpg', upload_to='badges_pics')

    def __str__(self):
        return f'{self.title} Badge'

class BadgeAcheiver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["user", "badge"]

    def __str__(self):
        return f'{self.user.username} Achieved {self.badge.title} on {self.date}'
