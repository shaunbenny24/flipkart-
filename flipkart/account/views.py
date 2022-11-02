from distutils.log import Log
from django.shortcuts import redirect, render
from .models import *
from .mixins import MessageHandler
import random
from django.contrib.auth import login,logout,authenticate
from .form import LoginForm
from .models import UserProfile
from django.http import JsonResponse,HttpResponse
# Create your views here.


def register_view(request):
    form=LoginForm()
    if request.method=='POST':
        # phone_number=request.POST.get('phone_number')
        form=LoginForm(request.POST)
        if form.is_valid():
            phone_number=form.cleaned_data.get("phone")
            user=UserProfile.objects.create(phone=phone_number)
            user.save()
            print('---------')
            return redirect('login')
    return render(request,'base.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        try: 
            phone_number= request.POST.get('phone_number')
            profile=UserProfile.objects.get(phone=phone_number)
            num_gen=random.randint(1000,9999)
            profile.otp= num_gen
            profile.save()
            print('otp is : ',profile.otp)
            # message_handler=MessageHandler(phone_number,profile.otp)
            # message_handler.send_otp_on_phone()
            return redirect(f'/account/otp/{profile.uid}')
            # success=phone_number+' OTP is below'
            # return HttpResponse(success)
        except:
            return redirect('register')
    return render(request,'base.html')

def otp(request,uid):

     if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
        # otp=request.POST.get('otp')
            otp=form.cleaned_data.get('otp')
            profile=UserProfile.objects.get(uid=uid)
            if otp==profile.otp:
                login(request,profile)
                return redirect('/')
            return redirect(f'/otp/{uid}')
     form=LoginForm()
     return render(request,'base.html',{'form':form,'uid':uid})

def signout(request):
    logout(request)
    return redirect('home')

