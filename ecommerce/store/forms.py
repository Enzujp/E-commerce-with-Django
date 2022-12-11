from tkinter import Widget
from django import forms

from .models import Product, Order, SignUp

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address', 'zip_code', 'city', )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description_field', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'description_field': forms.Textarea(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
        }

class SignupForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ('first_name', 'last_name', 'address', 'zip_code', 'city','email',)
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'address': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'zip_code': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'city': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'email': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            # 'username': forms.TextInput(attrs={
            #     'class': 'w-full p-4 border border-gray-200'
            # }),
        }