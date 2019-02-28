from django.db import models

# Create your models here.

class Set(models.Model):
    setname=models.CharField('系统名字',max_length=64) #设置名称
    setvalue=models.CharField('系统设置',max_length=200)#设置值
    class Meta:
        verbose_name_plural='系统设置'
