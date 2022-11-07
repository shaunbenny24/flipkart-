
from django.db import models

# Crea

class Category(models.Model):
    title = models.TextField()
    image = models.ImageField()
  

    def __str__(self):
        return self.title





class Product(models.Model):
    title = models.TextField()
    companybname = models.TextField()
    slideimage = models.ImageField()
    slideimages = models.ImageField()
    pimage1 = models.ImageField()
    pimage2 = models.ImageField()
    pimage3 = models.ImageField()
    pimage4 = models.ImageField()
    pimage5 = models.ImageField()
    price = models.IntegerField() 
    disprice =  models.IntegerField() 
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def __str__(self):
        return self.title








