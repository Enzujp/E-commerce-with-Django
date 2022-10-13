from django.contrib import admin
from django.urls import path, include
from core.views import about, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name="about"),
    path('', include ("store.urls")),
    path('', index, name="index"),
    path('userprofile/', include ("userprofile.urls")),
    
]
