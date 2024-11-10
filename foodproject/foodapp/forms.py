from django import forms
from .models import customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput , TextInput



# the form i screated by django userform

class userForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'email', 'password1','password2']
 


class regesterform(forms.ModelForm):
    
    class Meta:
        model = customer
        fields = ('username', 'email', 'phone', 'password')
        
        
# login process
class loginform(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput)
