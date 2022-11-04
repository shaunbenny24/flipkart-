from django.urls import path
from . import views

urlpatterns = [
    path ('cart', views.cart, name = 'cart'),
    path ('subcart/',views.subcart, name ='subcart'),
    path ('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path ('remove/<int:product_id/',views.cart_remove),
    path ('cart_detail',views.cart_detail, name='cart_detail'),
    path ('subcart_detail',views.subcart_detail, name='subcart_detail')


]
 