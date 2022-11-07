from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .forms import Personal_informationform,Address
from .models import Personal_information
from django.http import HttpResponse



def profile(request):
        form = Personal_informationform()
        if request.method == 'POST':
            form = Personal_informationform(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.user=request.user
                print(user.user,'=============')
                user.save()
                
                return redirect("profile")

        return render(request,'User/profile.html',{'form':form})


def manage(request):
        form = Address()
        if request.method == 'POST':
            form = Address(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.user=request.user
                print(user.user,'=============')
                user.save()
                # manage(request,user)
                
                return redirect("manage")

        return render(request,'User/manage.html',{'form':form})

# def manage(request):
#         registration = Address()
#         if request.method == 'POST':
#             form = Address(request.POST)
#             if form.is_valid():
#                 user = form.save(commit=False)

#                 user.save()      
#                 phone = form.cleaned_data['phone']
#                 pcode = form.cleaned_data['pcode']
#                 locality = form.cleaned_data['locality']
#                 address = form.cleaned_data['address']
#                 area = form.cleaned_data['area']
#                 state = form.cleaned_data['state']
#                 landmark = form.cleaned_data['landmark']
#                 anotherphone = form.cleaned_data['anotherphone']

#                 User_Profile = Address(
#                     user = user,
#                     phone = phone,
#                     pcode = pcode,
#                     locality = locality,
#                     address = address,
#                     area = area,
#                     state = state,
#                     landmark = landmark,
#                     anotherphone = anotherphone

#                 )
#                 User_Profile.save()

#                 manage(request,user)
#                 return render(request,'User/profile.html')
#             else:
#                 return render(request,'User/manage.html',{'form':form})

#         return render(request,'User/manage.html',{'form':registration})

    
            
    