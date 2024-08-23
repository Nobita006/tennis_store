from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Product, Cart

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'cart.html', {'cart': cart})
