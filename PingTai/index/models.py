from django.db import models

# Create your models here.

#用户表
class Users(models.Model):
    #id=models.IntegerField(primary_key=True)
    username=models.CharField(max_length=20,null=False,unique=True)
    password=models.CharField(max_length=20,null=False)
    email=models.EmailField(null=False)

