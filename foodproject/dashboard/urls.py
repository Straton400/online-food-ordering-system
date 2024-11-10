from django.urls import path

from . import views

app_name = 'admin dashboad'

urlpatterns = [
    path("home_dashboard", views.home_dashboard, name= 'home_dashboard')
]

