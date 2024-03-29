from django.db import models
from django.contrib.auth.models import User


class Userprofile(models.Model):
    """Userprofile class to seperate vendors from customers"""
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    is_vendor = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username