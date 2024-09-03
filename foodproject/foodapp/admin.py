from django.contrib import admin

from .models import customer

# Register your models here.l

class customerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'password')
  

admin.site.register(customer, customerAdmin)
