from django.shortcuts import render
from .forms import CheckoutForm

# Create your views here.
from django.shortcuts import render, redirect
from .models import Product, Category
from django.http import HttpResponse

# Homepage View
def homepage(request):
    categories = Category.objects.all()
    return render(request, 'ecommerce_app/homepage.html', {'categories': categories})

# Product Page View
def product_page(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'ecommerce_app/product_page.html', {'product': product})

# Cart Page View
def cart_page(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cart = request.session.get('cart', {})
        cart[product_id] = cart.get(product_id, 0) + 1  # Increment quantity
        request.session['cart'] = cart
        return redirect('cart_page')
    
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    return render(request, 'ecommerce_app/cart_page.html', {'cart': cart, 'products': products})

# Checkout Page View
from .forms import CheckoutForm

def checkout_page(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process the order here
            return redirect('confirmation_page')
    else:
        form = CheckoutForm()
    return render(request, 'ecommerce_app/checkout_page.html', {'form': form})

# Confirmation Page View
def confirmation_page(request):
    return render(request, 'ecommerce_app/confirmation_page.html')
