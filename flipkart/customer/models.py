from django.db import models
from account.models import UserProfile

class Personal_information(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    # user = models.OneToOneField(Personal_information,models.CharField(max_length=30))
    def __str__(self) :
        return self.first_name

class Address(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    username  = models.CharField(max_length=30)
    phone = models.IntegerField()
    pcode = models.IntegerField()
    locality = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    landmark = models.CharField(max_length=30)
    anotherphone = models.CharField(max_length=30)

    



    
