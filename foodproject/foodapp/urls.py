from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.auth  import views as auth_views



urlpatterns = [
    path("", views.home, name='home'),
    path("regester/",views.regester, name='regester'),
    path("login/",views.login, name='login'),
    path("about/", views.about, name='about'),
    path("<int:pk>/",views.details,name='details' ),
    path("order/",views.order, name='order'),
    path("regester2", views.regester2, name='regester2'),
    path("logout/", views.logout, name='logout'),
    path("menu_list/", views.menu_list, name='menu_list'),
    
    
    # add to the cart links
    path("cart-summary/",views.cart_add, name='cart_add'),
    path("add/",views.cart_add, name='cart_add'),
    path("delete/",views.cart_delete, name='cart_delete'),
    path("update/",views.cart_update, name='cart_update'),
    
    
    
    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
