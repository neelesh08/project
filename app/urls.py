
from django.urls import path , include
from . import views
urlpatterns = [
    path("",views.app,name="login"),
    path("login",views.login),
    path("led",views.led)
]   
