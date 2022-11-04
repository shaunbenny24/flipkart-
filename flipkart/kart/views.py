from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from product.models import Product
from .cart import Cart
from .forms import CartAddProductForm


# Create your views here.
def cart(request):
    return render(request,'cart/cart.html')

def subcart(request):
    product =Product.objects.all()
    return render(request,'cart/subcart.html',{'product':product})

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    print(form)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
        print(cart)
    return redirect('cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    # for item
    
    return render(request, 'cart/cart.html',{'cart':cart})
def subcart_detail(request):
    cart = Cart(request)
    print(Cart)
    return render(request,'cart/subcart.html',{'cart':cart})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id,slug=slug,available=True)

    cart_product_form = CartAddProductForm()
    return render(request,'product/productdetail.html', {'product':product, 'cart_product_form':cart_product_form})


