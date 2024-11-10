from django.shortcuts import render, redirect

# Create your views here.

def home_dashboard(request):
    return render(request, 'home_dashboard.html')
