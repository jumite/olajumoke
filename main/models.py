from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AppInfo (models.Model):
    appname = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo')
    carousel1 = models.ImageField(upload_to='carousel1')
    carousel2 = models.ImageField(upload_to='carousel2')
    carousel3 = models.ImageField(upload_to='carousel3')
    banner = models.ImageField(upload_to='banner')
    copyright = models.IntegerField()
    
    def __str__(self):
        return self.appname
    
    
class Category (models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    img = models.ImageField(upload_to='cating')
    
    def __str__(self):
        return self.name
    
    
class Product (models.Model):
    category = (models.ForeignKey(Category, on_delete=models.CASCADE))
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    pix = models.ImageField(upload_to='pix')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    description = models.TextField()
    featured = models.BooleanField(default=False)
    uploaded = models.DateField(auto_now=True)
    edited = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    messages = models.TextField()
    sent = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.full_name
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=150)
    pix = models.ImageField(upload_to='pix')
    joined = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'customer'
        managed = True
        verbose_name = 'Customer'
        verbose_name_plural = 'Customer'
        
        
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    furniture = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.CharField(max_length=10)
    quantity = models.IntegerField()
    paid =models.BooleanField()
        
    def __str__(self):
        return self.user.username
    
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    amount = models.IntegerField()
    paid = models.BooleanField()
    pay_code = models.CharField(max_length=50)
    purchase_date= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
            
    