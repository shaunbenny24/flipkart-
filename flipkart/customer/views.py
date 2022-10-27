from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request,'User/profile.html')

def manage(request):
    return render(request,'User/manage.html')