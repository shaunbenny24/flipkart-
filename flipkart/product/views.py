from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def product(request):
    return render(request,'product/productlist.html')
def  productdescrip(request):
    return render(request,'product/productdetail.html')