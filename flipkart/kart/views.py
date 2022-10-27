from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cart(request):
    return render(request,'cart/cart.html')

def subcart(request):
    return render(request,'cart/subcart.html')
