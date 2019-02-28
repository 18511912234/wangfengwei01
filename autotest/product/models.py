from django.db import models

# Create your models here.

class Product(models.Model):
    productname=models.CharField('产品名称',max_length=64,null=False)
    productdescription=models.CharField('产品描述',max_length=200,null=False)
    producter=models.CharField('测试人员',max_length=20,null=False)
    create_time=models.DateTimeField('创建时间',auto_now=True)

    class Meta:
        verbose_name_plural="产品管理"
