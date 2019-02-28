from django.db import models
from product.models import Product
# Create your models here.

#流程接口表
class Apitest(models.Model):
    Product=models.ForeignKey('product.Product',on_delete=models.CASCADE)#关联的产品id
    apitestname=models.CharField('流程接口名',max_length=64)#流程接口测试场景
    apitestdesc=models.CharField('描述',max_length=64)#流程接口描述
    apitester=models.CharField('测试负责人',max_length=16)#测试负责人
    apitestresult=models.BooleanField('测试结果')#流程测试结果
    create_time=models.DateTimeField('创建时间',auto_now=True)#创建时间

    class Meta:
        verbose_name_plural='流程场景接口'


#接口表
class Apistep(models.Model):
    Apitest=models.ForeignKey(Apitest,on_delete=models.CASCADE)#关联接口ID
    apiname=models.CharField('接口标题',max_length=100)#接口名字
    apiurl=models.CharField('url地址',max_length=200)#接口地址
    apistep=models.CharField('接口测试步骤',max_length=100,null=True)#测试步骤
    apiparamvalue = models. CharField('请求参数和值',max_length=800) #请求参数和值
    REQUEST_METHOD=(('get','get'),('post','post'))
    apimethod=models.CharField(verbose_name='请求方法',choices=REQUEST_METHOD,default='get',max_length=200,null=True) #请求方法
    apiresult=models.CharField('预期结果',max_length=200) #预期结果
    apiresponse=models.CharField('响应结果',max_length=5000,null=True)#响应结果
    apistatus=models.BooleanField('是否通过')#测试结果
    create_time=models.DateTimeField('创建时间',auto_now=True)

#单一接口表
class Apis(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)  # 关联的产品id
    apiname = models.CharField('接口标题', max_length=100)  # 接口名字
    apiurl = models.CharField('url地址', max_length=200)  # 接口地址
    apiparamvalue = models.CharField('请求参数和值', max_length=800)  # 请求参数和值
    REQUEST_METHOD = (('0', 'get'), ('1', 'post'))
    apimethod = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD, default='0', max_length=200)  # 请求方法
    apiresult = models.CharField('预期结果', max_length=200)  # 预期结果
    apistatus = models.BooleanField('是否通过')  # 测试结果
    create_time = models.DateTimeField('创建时间', auto_now=True) #创建时间
    producter=models.CharField('产品负责人',max_length=200,null=True)#产品负责人

    class Meta:
        verbose_name_plural="单一场景接口"