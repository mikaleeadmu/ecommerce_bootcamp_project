from django.urls import path
from .views import homepage, product_page, cart_page, checkout_page, confirmation_page

urlpatterns = [
    path('', homepage, name='homepage'),
    path('product/<int:product_id>/', product_page, name='product_page'),
    path('cart/', cart_page, name='cart_page'),
    path('checkout/', checkout_page, name='checkout_page'),
    path('confirmation/', confirmation_page, name='confirmation_page'),
]