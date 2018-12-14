from django.db import models

# Create your models here.

# class Product(models.Model):
#     name=models.CharField(max_length=50)
#     type=models.CharField(max_length=20)


#一对一：第1张表的某一行数据只能与第2张表的某一样数据对应，第2张表的某一行数据也只能与第1张表的某一行数据对应
# class Performer(models.Model):
#     name=models.CharField(max_length=20)
#     nationality=models.CharField(max_length=20)
#     masterpiece=models.CharField(max_length=50)

# class Performer_info(models.Model):
#     performer=models.OneToOneField(Performer,on_delete=models.CASCADE) #一对一
#     birth=models.CharField(max_length=20)
#     elapse=models.CharField(max_length=20)

#一对多：第1张表的某一行数据可以与第二个表的一到多行数据进行关联，第二张表的某一行数据也可以与第1张表的1到多行对应

class Performer(models.Model):
    name=models.CharField(max_length=20)
    nationality=models.CharField(max_length=20)

class Program(models.Model):
    performer=models.ForeignKey(Performer,on_delete=models.CASCADE) #一对多添加外键
    name=models.CharField(max_length=20)

class Type(models.Model):
    pass
class Product(models.Model):
    pass


#多对多：同理->他会自动生成第三张关联的表
# class Performer(models.Model):
#     name=models.CharField(max_length=20)
#     nationality=models.CharField(max_length=20)
#
# class Program(models.Model):
#     name=models.CharField(max_length=20)
#     performer=models.ManyToManyField(Performer)#用ManyToManyField来构建数qa据表多对多的关系