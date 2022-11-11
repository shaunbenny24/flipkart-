from django.db import models
<<<<<<< Updated upstream
from customer.models import Address,Personal_information,UserProfile
from product.models import Product
from account.models import UserProfile
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    address=models.ForeignKey(Address,on_delete=models.CASCADE,related_name='order_ad')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    paid=models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'user is : {self.address.user}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    selections =(
    ("pending", "pending"),
    ("Order Confirmed", "Order Confirmed"),
    ("Shipped", "Shipped"),
    ("Out For Delivery", "Out For Delivery	"),
    ("Delivered", "Delivered"),
)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_items')
    price=models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length=20,
        choices=selections,
        default='pending',)

    
    def __str__(self):
        return f'item is : {self.product.title}'

    def get_cost(self):
        return self.price * self.quantity

    def order_list(self):
        user=self.order.all()
        my_list=OrderItem.objects.filter()
=======
from customer.models 
# Create your models here.

class Order(models.Model):
    address=
>>>>>>> Stashed changes
