from django.db import models

# Create your models here.

class customer(models.Model):
    username = models.CharField(max_length=121)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=200)
    password = models.CharField( max_length=100)
    
    
    def __str__(self):
        return f"{self.username} - {self.email} - {self.phone} - {self.password}"

class categories(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class menu(models.Model):
    categories = models.ForeignKey(categories, related_name='menu', on_delete=models.CASCADE)
    name = models.CharField(max_length=222)
    discription = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='menu-images', blank=True, null=True)
    is_available = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
   
    def __str__(self):
        return f"{self.categories} - {self.name} - {self.discription}- {self.image} - {self.price}"


 

