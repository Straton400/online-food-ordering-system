from django.contrib import admin

from .models import customer, categories,menu

# Register your models here.l

class customerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'password')
  

admin.site.register(customer, customerAdmin)


class menuAdmin(admin.ModelAdmin):
    list_display = ('categories', 'name', 'discription', 'price','image')
  
admin.site.register(menu,menuAdmin)

admin.site.register(categories)
        