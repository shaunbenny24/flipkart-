from django.urls import path
from . import views

urlpatterns = [
    path ('cart', views.cart, name = 'cart'),
    path ('subcart/',views.subcart, name ='subcart'),

]
 