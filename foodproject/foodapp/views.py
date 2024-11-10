from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import regesterform, loginform, userForm

from .models import menu, categories 

# for authentication
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.


# regester vierw to regester the user created by default django models

def regester2(request):
    
    form = userForm()
    
    if request.method == "POST":
        
        form = userForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('login')
        
        
        
    return render (request, 'regester2.html', {'form':form})


# this is for home page
def home(request):
    menus = menu.objects.filter(is_available = False)[0:8]
    categoriess = categories.objects.all()
    return render(request, "home.html",{
        'categoriess': categoriess,
        'menus': menus,
    })

# details page

def details(request, pk):
    menus = get_object_or_404(menu, pk=pk)
    
    return render(request, 'details.html',{
        'menus':menus
    })
    
# regestretion
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
            
            
            user= authenticate(request, username= username, password=password)
            
            if user is not None:
                
                auth.login(request, user)
                
                return redirect('order')
    
    context = {'loginform': form}
        
    return render(request, 'login.html', context=context)


# this is about page
def about(request):
    return render(request, 'about.html')


# this is for oder page
def order(request):
    return render(request, 'order.html')
 

# this is for log out
def logout(request):  
    auth.logout(request)
    
    return redirect('')


# this is viewis for menu list

@login_required
def menu_list(request):
    menus = menu.objects.filter(image=request.user)
    
    
    return render(request, 'menu_list.html',{'menus': menu})
 

# creat view for add to cart urls

def cart_add(request):
    return render(request, 'iii.html')
 
def cart_delete(request):
    return render(request, 'iii.html')
 
def cart_update(request):
    return render(request, 'iii.html')

def cart_sammary(request):
    return render(request, 'iii.html')
 

