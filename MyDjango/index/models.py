from django.db import models
from django.utils.html import format_html
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
    type_name=models.CharField(max_length=20,verbose_name="类型")
    #设置返回值
    def __str__(self):
        return self.type_name

    class Mate:
        verbose_name_plural = "产品类型"

class Product(models.Model):
    name=models.CharField("商品名字",max_length=50)
    weight=models.CharField("商品宽度",max_length=20)
    height=models.CharField("商品高度",max_length=20)
    type=models.ForeignKey(Type,on_delete=models.CASCADE,verbose_name="商品类型")

    #重写__str__设置返回值
    def __str__(self):
        return self.name

    #定义Meta类来设置模型类的中文名字
    class Meta:
        verbose_name_plural="产品信息"

    #自定义函数，设置字体颜色
    #导入from django.utils.html import format_html
    def colored_type(self):
        if "华为" in self.type.type_name:
            color_code="red"
        elif "小米" in self.type.type_name:
            color_code="green"
        else:
            color_code='yellow'
        return format_html(
            '<span style="color:{};"> {} </span>',color_code,self.type
        )















#多对多：同理->他会自动生成第三张关联的表
# class Performer(models.Model):
#     name=models.CharField(max_length=20)
#     nationality=models.CharField(max_length=20)
#
# class Program(models.Model):
#     name=models.CharField(max_length=20)
#     performer=models.ManyToManyField(Performer)#用ManyToManyField来构建数qa据表多对多的关系