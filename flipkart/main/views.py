
from django.shortcuts import render
from django.http import HttpResponse
from product.models import Category,Product


# Create your views here.
def index(request):

    products = Product.objects.all()
    categorys = Category.objects.all()

    return render(request,'index.html',{'products':products,'categorys': categorys})

         
         
         
            