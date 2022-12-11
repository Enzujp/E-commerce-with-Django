from tkinter import ACTIVE
from django.db import models

from django.contrib.auth.models import User

from django.core.files import File

from io import BytesIO
from PIL import Image


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
    thumbnail = models.ImageField(upload_to='uploads/product_images/thumbnails', blank=True, null=True)
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

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        thumb_io = BytesIO()
        if img.mode in ("RGBA", "P"):
            img = img.convert('RGB')
        img.thumbnail(size)
    
        
        img.save(thumb_io, 'JPEG', quality=85)
        name = image.name.replace('uploads/product_images/', '')
        thumbnail = File(thumb_io, name=image.name)

        return thumbnail


    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'

class Order(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    total_cost = models.IntegerField(default=0)
    paid_amount = models.IntegerField(blank=True, null=True)
    merchant_id = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL,  null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="items", on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)

class SignUp(models.Model):
    created_by = models.OneToOneField(User, related_name="signup", null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    # username = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=250)
    zip_code = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    password = models.CharField(max_length=30)
    as_vendor = models.BooleanField(default=False)
    email = models.CharField(max_length=200, null=True)