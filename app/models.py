from django.db import models
from django import forms

# Create your models here.
class datebase(models.Model,forms.ModelForm):
    user = models.CharField(max_length=10)
    firstname  =  models.CharField()
    lastname =models.CharField()
    email = models.EmailField( max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)

