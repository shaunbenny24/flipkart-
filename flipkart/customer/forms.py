from distutils.command.clean import clean
import numbers
from django import forms
from .models import Personal_information,Address
# class Address(forms.ModelForm):
   
#     username  = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"username"}))
#     phone = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"phonenumber"}))
#     pcode = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"pincode"}))
#     locality = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"locality"}))
#     address = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"address",'class':'wid'}))
#     area = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"area"}))
#     state = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"state"}))
#     landmark = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"landmark"}))
#     anotherphone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"alternative phone"}))

#     # user = forms.OneToOneField(UserProfile,on_delete=forms.CASCADE)


class Personal_informationform(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"last name"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"email"}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"Mobile Number"}))
        
    class Meta:
        model= Personal_information
        exclude= ('user',)
  
    # user = forms.OneToOneField(UserProfile,on_delete=forms.CASCADE)

class Address(forms.ModelForm):
    username  = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"username"}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"phonenumber"}))
    pcode = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"pincode"}))
    locality = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"locality"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"address",'class':'wid'}))
    area = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"area"}))
    state = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"state"}))
    landmark = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"landmark"}))
    anotherphone = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"alternative phone"}))
            
    class Meta:
        model= Address
        exclude= ('user',)
        