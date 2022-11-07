from dataclasses import fields
from django import forms
from .models import UserProfile



class LoginForm(forms.ModelForm):
    
    class Meta:
        model=UserProfile
        fields=['phone','otp']

        widgets={
            'phone':forms.TextInput(attrs={'name':'phone_number','placeholder':"Enter PhoneNumber"}),
            'otp':forms.TextInput(attrs={'name':'otp'})
        }