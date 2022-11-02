from email.policy import default
from tokenize import blank_re
from django.db import models
# from django.contrib.auth.models import User
import uuid
# # Create your models here.
# class Profile(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
#     phone_number=models.CharField(max_length=15)
#     otp= models.CharField(max_length=20,blank=True)
#     uid= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """ Create a new user profile """
        if not phone:
            raise ValueError('User must have an email address')

        
        user = self.model(phone=phone)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone, password):
        """ Create a new superuser profile """
        user = self.create_user(phone, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    phone =models.CharField(max_length=20,unique=True,blank=True)
    otp= models.CharField(max_length=20,blank=True)
    uid= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_staff = models.BooleanField(default=True)
    

    objects = UserProfileManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        """ Return string representation of our user """
        return self.phone
