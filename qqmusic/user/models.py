from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    qq=models.CharField('qq号码',max_length=11)
    weChar=models.CharField('微信号码',max_length=15)
    mobile=models.CharField('手机号',max_length=11,unique=True)

    def __str__(self):
        return self.username
