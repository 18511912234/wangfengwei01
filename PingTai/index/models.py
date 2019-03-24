from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=10, null=False, unique=True)
    password = models.CharField(max_length=10, null=False)
    email = models.EmailField(null=False)

class Cases(models.Model):
    name = models.CharField(max_length=10, null=False, unique=True)
    desc = models.CharField(max_length=50, null=True)
    method = models.CharField(default='get', max_length=10)
    url = models.URLField(null=False)
    headers = models.TextField(null=True)
    body_type = models.CharField(default='none', max_length=20)
    body_value = models.TextField(null=True)
    checks = models.TextField(null=False)

class Task(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)
    description = models.CharField(max_length=50, null=True)
    cases = models.ManyToManyField(Cases)
