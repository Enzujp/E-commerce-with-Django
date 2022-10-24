from tkinter import ACTIVE
from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    DRAFT = 'draft'
    WAITING_APPROVAL = 'waitingapproval'
    ACTIVE = 'active'
    DELETED = 'deleted'

    STATUS_CHOICES= (
        (DRAFT, 'draft'),
        (WAITING_APPROVAL, 'Waiting approval'),
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted')
    )

    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/product_images', blank=True, null=True)
    slug = models.SlugField(max_length=50)
    description_field = models.TextField(null=True)
    price = models.IntegerField()
    time_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)


    class Meta:
        ordering = ('-time_created',)

    def __str__ (self):
        return self.title 