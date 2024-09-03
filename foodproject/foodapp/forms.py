from django import forms

from .models import customer
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput , TextInput


class regesterform(forms.ModelForm):
    
    class Meta:
        model = customer
        fields = ('username', 'email', 'phone', 'password')
        
        
# login process

class loginform(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput)