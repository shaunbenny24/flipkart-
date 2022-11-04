from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Category,Product
from kart.forms import CartAddProductForm
# Create your views here.
def product(request,id=None):
 if id:
        category = get_object_or_404(Category,id=id)
        descrips = Product.objects.filter( Category  = category)

        return render(request,'product/productlist.html',{'descrips':descrips} )

 else:
        descrips =Product.objects.all()
        return render(request,'product/productlist.html',{'descrips':descrips}  )


def  productdescrip(request,id):
        productdetail = Product.objects.get(id=id)
        form=CartAddProductForm()
        return render(request,'product/productdetail.html',{'productdetail':productdetail,'form':form})