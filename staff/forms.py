from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from products.models import Product


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ['category','title','slug','stock','description','image','price']