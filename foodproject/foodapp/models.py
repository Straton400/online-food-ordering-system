from django.db import models

# Create your models here.

class customer(models.Model):
    username = models.CharField(max_length=121)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=200)
    password = models.CharField( max_length=100)
    
    
    def __str__(self):
        return f"{self.username} - {self.email} - {self.phone} - {self.password}"
    
class menu(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    
    
class menu_item(models.Model):
    menu_id = models.ForeignKey(menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to="menu_images", blank=True, null=True)
    
class orders(models.Model):
    customer_id = models.ForeignKey(customer,on_delete=models.CASCADE )
    total_price = models.CharField(max_length=200)
    order_date = models.DateField 
    status = models.CharField (max_length=100)    
