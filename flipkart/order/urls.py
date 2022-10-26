from django.urls import path, include
from . import views
urlpatterns = [
    path('all/',views.order_list,name='order_list')
    ]