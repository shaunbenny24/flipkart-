
from django.shortcuts import render
from django.http import HttpResponse
from product.models import Category,Product
from kart.cart import Cart

# Create your views here.
def index(request):

    products = Product.objects.all()
    categorys = Category.objects.all()
    cart = Cart(request)
    print(cart)
    context = {'products':products,'categorys': categorys, 'cart':cart}
    return render(request,'index.html',context)

         
         
         
            