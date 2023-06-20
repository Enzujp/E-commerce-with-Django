from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .cart import Cart
from .forms import OrderForm
from .models import Product, Category, Order, OrderItem


def add_to_cart(request, product_id):
# This function allows users add product to cart
    cart = Cart(request)
    cart.add(product_id)

    return redirect('cart_view')

def change_quantity(request, product_id):
# This functioin allows users increase or decrease quantity of item(s) in cart
    action = request.GET.get('action', '')

    if action:
        quantity = 1

        if action == 'decrease':
            quantity = -1

        cart = Cart(request)
        cart.add(product_id, quantity, True)

    return redirect('cart_view')

def remove_from_cart(request, product_id):
# This function allows users remove items from cart
    cart = Cart(request)
    cart.remove((product_id) )

    return redirect('cart_view')

def cart_view(request):
    cart = Cart(request)

    return render(request, 'store/cart_view.html', {
        'cart': cart
    })


@login_required
def checkout(request):
# This function allows users finalize shopping and checkout products from shopping cart
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            total_price = 0

            for item in cart:
                product = item['product']
                total_price += product.price * int(item['quantity'])

            order = form.save(commit=False)
            order.created_by = request.user
            order.paid_amount = total_price
            order.save()

            for item in cart:
                product = item['product']
                quantity = int(item['quantity'])
                price = product.price * quantity
                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)
            
            cart.clear()

            return redirect('myaccount')
    else:
        form = OrderForm()
    return render(request, 'store/checkout.html', {
        'cart': cart,
        'form': form
    })


def search(request):
# This function allows users search for specific goods, from the list or range of available products
    query = request.GET.get('query', '')
    products = Product.objects.filter(status=Product.ACTIVE).filter(Q(title__icontains=query) | Q(description_field__icontains=query))
    return render(request, 'store/search.html', {
        'query': query,
        'products': products
    })


def category_detail(request, slug):
# This function displays available products based on the available categories
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'store/category_detail.html', {
        'category': category,
        'products': products
    } )

def product_detail(request, category_slug, slug):
# This function allows users view more information on particular products that they desire.

    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)

    return render(request, 'store/product_detail.html', {
        'product': product
    })