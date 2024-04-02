from django.db import models
from datetime import datetime

# Create your models here
class Customer(models.Model):
    Name=models.CharField(max_length=100)
    Image=models.ImageField(upload_to="images/")
    Email=models.EmailField
    Created_at=models.DateField(default=datetime.now)
    def __str__(self):
        return self.Name
class Auth(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=120)
    Password=models.CharField(max_length=50)
    Dob=models.DateField()
    Image=models.ImageField(upload_to="auth/images")
    def __str__(self):
        return self.Name