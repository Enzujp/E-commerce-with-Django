from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Product, Order, User

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

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.TextInput()
    last_name = forms.TextInput()

    class Meta:
        model = User
        fields = ( "first_name", "last_name", "username", "email", "password1", "password2")


        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'last_ name': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'username': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
        }



    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user




    