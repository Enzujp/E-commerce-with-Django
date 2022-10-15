from django.urls import path

from .import views

urlpatterns = [
    path('vendors/<int:pk>/', views.vendor_detail, name="vendor_detail")
]