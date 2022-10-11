from django.urls import path

from userprofile.views import index

urlpatterns = [
    path('', index, name="index"),
]