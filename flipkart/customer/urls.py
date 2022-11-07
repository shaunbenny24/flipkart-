from unicodedata import name
from django.urls import path , include
from .import views


urlpatterns = [
    path('',views.profile, name = "profile"),
    path('manage/',views.manage, name = "manage"), 
]
