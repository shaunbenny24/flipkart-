# from django.db import models
# from django.contrib.auth.models import User
# from datetime import datetime
# from product.models  import Product
# # from core.models import product

# # Create your models here.
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(default=datetime.now)


# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     price_ht = models.FloatField(blank=True)
#     cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
