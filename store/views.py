from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
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
    query = request.GET.get('q') or ''
    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    paginator = Paginator(products, 10)  # Show 10 products per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products.html', {'page_obj': page_obj, 'query': query})

def view_cart(request):
    cart = Cart.objects.get(user=request.user)
    return render(request, 'cart.html', {'cart': cart})

def custom_logout(request):
    logout(request)
    return redirect('login')