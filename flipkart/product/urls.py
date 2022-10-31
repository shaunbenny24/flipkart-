from django.urls import path
from . import views

urlpatterns = [
    path ('product/', views.product, name = 'emp'),
    path ('product/<int:id>', views.product ,name = 'product'),
    path ('productdes/<int:id>', views.productdescrip, name = 'productdetail'),


]
 