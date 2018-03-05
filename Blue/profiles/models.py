from django.db import models
from django.contrib import auth
# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username

# Incomplete
# class Profile(models.Model):
#     name = models.CharField(max_length = 100)
#     varsity_id = models.CharField(max_length = 20, unique = True)
#     sheet_id = models.IntegerField(default = 0)
#
#     def __str__(self):
#         return self.name + ' ( ' + self.varsity_id + ' ) '
