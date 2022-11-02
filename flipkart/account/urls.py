from django.urls import path, include
from . import views
urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    path('otp/<uid>/',views.otp,name='otp'),
    path('logout/',views.signout,name='logout')
  ]