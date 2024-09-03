from django.urls import path, include

from .import views


urlpatterns = [
    path("", views.home, name='home'),
    path("regester/",views.regester, name='regester'),
    path("login/",views.login, name='login'),
]
