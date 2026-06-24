from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Product, Order


def home(request):
    products = Product.objects.all()

    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains=search)

    return render(request, 'home.html', {'products': products})


def product_detail(request, id):

    product = get_object_or_404(Product, id=id)

    similar_products = Product.objects.filter(
        category=product.category
    ).exclude(id=id)[:4]

    return render(request, 'product.html', {
        'product': product,
        'similar_products': similar_products
    })


def add_to_cart(request, id):

    cart = request.session.get('cart', [])

    id = int(id)

    if id not in cart:
        cart.append(id)

    request.session['cart'] = cart

    return redirect('/cart/')


def remove_from_cart(request, id):

    cart = request.session.get('cart', [])

    id = int(id)

    if id in cart:
        cart.remove(id)

    request.session['cart'] = cart

    return redirect('/cart/')


@login_required
def cart(request):

    cart_ids = request.session.get('cart', [])

    products = Product.objects.filter(id__in=cart_ids)

    return render(request, 'cart.html', {'products': products})


@login_required
def checkout(request):
    return render(request, 'checkout.html')


@login_required
def success(request):

    cart_ids = request.session.get('cart', [])

    if not cart_ids:
        return render(request, 'success.html')

    products = Product.objects.filter(id__in=cart_ids)

    for product in products:
        Order.objects.create(
            user=request.user,
            product=product,
            quantity=1,
            total_price=product.price
        )

    request.session['cart'] = []

    return render(request, 'success.html')


def men(request):
    products = Product.objects.filter(category="Men")
    return render(request, 'home.html', {'products': products})


def women(request):
    products = Product.objects.filter(category="Women")
    return render(request, 'home.html', {'products': products})


@login_required
def orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': orders})


def register_page(request):

    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return redirect('/register/')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/login/')

    return render(request, 'register.html')


def login_page(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/') 
def accessories(request):
    products = Product.objects.filter(category="Accessories")
    return render(request, 'home.html', {'products': products})