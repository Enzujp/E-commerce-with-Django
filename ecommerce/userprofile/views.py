from telnetlib import STATUS
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.utils.text import slugify
from django.shortcuts import get_object_or_404

from core.views import index
from .models import Userprofile
from store.forms import ProductForm, SignupForm
from store.models import Product, Category, Order, OrderItem, User


# This view yields vendor details and their uploaded, available products.
def vendor_detail(request, pk):
    user = User.objects.get(pk)
    products = user.products.filter(status=Product.ACTIVE)

    return render(request, 'userprofile/vendor_detail.html', {
        'user': user,

        'products': products
    })
     
   
@login_required
# This function displays products belonging to a vendor, as well as their pending orders
def my_store(request):
    products = request.user.products.exclude(status=Product.UNSORTED)
    # products = request.user.products.exclude(status=Product.SORTED)
    order_items = OrderItem.objects.filter(product__user=request.user)
    return render(request, 'userprofile/my_store.html', {
        'products': products,
        'order_items': order_items
    })

def sorted(request, pk):
# This function lets vendors sort and separating what products they've cleared from their list of pending orders
    order_item = OrderItem.objects.filter(product__user=request.user).get(pk=pk)
    order_item = order_item.SORTED # try mapping this for the sorted part
    messages.success(request, 'This item has been sorted')
    return redirect ('my_store')


def my_sales(request):
# This function shows vendors what products have been sold and their total gains
    products = request.user.products.exclude(status=Product.SORTED)
    order_items = OrderItem.objects.filter(product__user=request.user)
    return render(request, 'userprofile/sales.html', {
        'products': products,
        'order_items': order_items
    })


@login_required
# This function displays the specifics for an order
def my_store_order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'userprofile/my_store_order_detail.html', {
        'order': order
    })


@login_required
# This function allows vendors add new product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify('title')
            product.save()

            messages.success(request, "The product was added!")

            return redirect('my_store')
    else:
        form = ProductForm()
    form = ProductForm()
    return render (request, 'userprofile/product_form.html', {
        'form': form,
        'title': 'Add product'
    })

@login_required
# This function allows vendors edit already uploaded products
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, 'The changes were saved!')
            return redirect('my_store')
    
    else:
        form = ProductForm(instance=product)
    return render (request, 'userprofile/product_form.html', {
        'form': form,
        'product': product,
        'title': 'Edit product'
    })


@login_required
# This function allows a vendor delete or remove an uploaded product.
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = product.DELETED
    product.save()
    messages.success(request, 'This item has been deleted!')
    return redirect('my_store')
    


@login_required
# This funtion directs users directly to their accounts, where they can access functionalities tailored to their account type
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')



def signup(request):
# This function lets users signup for new accounts
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            messages.success(request, 'Registration was successful!')

            return redirect('index')
            

    else:
        form = SignupForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })