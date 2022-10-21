from django import forms

from .models import Product 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description_field', 'price', 'image',)    