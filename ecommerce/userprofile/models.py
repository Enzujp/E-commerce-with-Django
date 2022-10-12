from msvcrt import open_osfhandle
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username