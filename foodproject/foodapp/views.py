from django.shortcuts import render, redirect

from .forms import regesterform, loginform

# for authentication
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, "home.html")


def regester(request):
    form = regesterform()
    
    if request.method== "POST":
        
        form = regesterform(request.POST)
        
        if form.is_valid():
            
            form.save()
            return redirect('login')
        
    return render(request, 'regester.html',{'form':form})


# login process

def login(request):
    
    form = loginform()
    
    if request.method == 'POST':
        form = loginform(request, data=request.POST)
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            
            customer= authenticate(request, username= username, password=password)
            
            if customer is not None:
                
                auth.login(request, customer)
                
                return redirect('home')
    
    context = {'loginform': form}
        
    return render(request, 'login.html', context=context)
