from django.conf import settings
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core.views import about, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name="about"),
    path('', include("userprofile.urls")),
    path('', include ("store.urls")),
    path('', index, name="index"),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
