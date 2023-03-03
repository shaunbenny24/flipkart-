from django.urls import path, include
from . import views
from django.urls import path, re_path
urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    path('otp/<uid>/',views.otp,name='otp'),
    path('logout/',views.signout,name='logout'),

    
    # path('login/',views.signin, name='login'),


    


  ]