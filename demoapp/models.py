from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)

class userlogin(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='user',null=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=30)
    address = models.TextField(max_length=200)
    phone = models.IntegerField(null=True,blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name

class productadd(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    prdid = models.CharField(max_length=30)
    type = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.CharField(max_length=30)
    description = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.name
