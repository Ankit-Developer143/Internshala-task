from django.forms import ModelForm 
from .models import Data

#import for login and registration form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class DataForm(ModelForm):
    class Meta:
        model = Data
        
        fields = '__all__'