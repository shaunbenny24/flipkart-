from django.shortcuts import render,redirect,HttpResponse
from kart.cart import Cart
from .models import OrderItem,Order
from customer.models import Address,Personal_information
from django.contrib.auth.decorators import login_required
# Create your views here.
def order_list(request):
    user= request.user
    order_list = Order.objects.filter(user=user)
    items=OrderItem.objects.filter(order__in=order_list)
   
    return render(request,'order/order_list.html',{'items':items})
   

def order_details(request):
    user= request.user
    order_list = Order.objects.filter(user=user)
    items=OrderItem.objects.filter(order__in=order_list)
    return render(request,'order/order_details.html',{'items':items})

@login_required(login_url='/account/login/')
def order_create(request):
    cart=Cart(request)
    user=request.user
    if Address.objects.filter(user=user).exists():
        address=Address.objects.get(user=user)
        order=Order.objects.create(address=address,user=user)
        order.save()

        for item in cart:
            OrderItem.objects.create(order=order,
            product=item['product'],
            price=item['price'],
            quantity=item['quantity']
            )
        cart.clear()
        context={'order':order,
        'cart':cart
        }
        # return render(request,'order/order_list.html',context)
        return redirect('order_list')

    else:
        return redirect('manage')


