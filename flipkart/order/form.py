from django import forms
from .models import Order

class OrderCreateForm(forms.Model):
    class Meta:
        model=Order
        fields='__all__'
