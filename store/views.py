from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Product, Cart, CartItem, Order, OrderItem
import json
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a suitable page after signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def product_list(request):
    query = request.GET.get('q') or ''
    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    paginator = Paginator(products, 9) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products.html', {'page_obj': page_obj, 'query': query})

def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart.html', {'cart': cart})

def custom_logout(request):
    logout(request)
    return redirect('login')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:  # Only increase quantity if the item already exists in the cart
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1
    cart_item.save()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'status': 'success'})
    
    return redirect('view_cart')

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')

def empty_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.items.all().delete()
    return redirect('view_cart')

def finalize_order(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    order = Order.objects.create(user=request.user, total_amount=sum(item.product.price * item.quantity for item in cart.items.all()))
    for item in cart.items.all():
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
    cart.items.all().delete()
    return redirect('view_order', order_id=order.id)

def view_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order.html', {'order': order})

def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.status = 'Cancelled'
    order.save()
    return redirect('view_order', order_id=order.id)

def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    total_amount = sum(item.product.price * item.quantity for item in cart.items.all())
    return render(request, 'cart.html', {'cart': cart, 'total_amount': total_amount})

def update_cart_item(request, cart_item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
        data = json.loads(request.body)
        cart_item.quantity = int(data.get('quantity', 1))
        cart_item.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

def pay_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # Simulate payment process
    # You could integrate with a real payment gateway here

    # After successful payment
    order.status = 'Paid'
    order.save()

    return redirect('view_order', order_id=order.id)

def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if order.status == 'Pending':
        # Get or create the user's cart
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Loop through the order items and add them back to the cart
        for order_item in order.orderitem_set.all():
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=order_item.product)
            
            # Directly set the quantity in the cart
            cart_item.quantity = order_item.quantity if created else cart_item.quantity + order_item.quantity
            cart_item.save()

        order.delete()  # Delete the order
        return redirect('view_cart')  # Redirect to cart page

    return redirect('view_order', order_id=order.id)