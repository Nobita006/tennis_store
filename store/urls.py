from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('products/', views.product_list, name='products'),
    path('cart/', views.view_cart, name='view_cart'),  # Ensure this name is 'view_cart'
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/empty/', views.empty_cart, name='empty_cart'),
    path('order/finalize/', views.finalize_order, name='finalize_order'),
    path('order/<int:order_id>/', views.view_order, name='view_order'),
    path('order/<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
    path('cart/update/<int:cart_item_id>/', views.update_cart_item, name='update_cart_item'),
    path('order/<int:order_id>/pay/', views.pay_order, name='pay_order'),
]