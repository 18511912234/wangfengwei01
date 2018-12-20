from django.contrib import admin
from .models import *
from index.models import Product as a
# Register your models here.

#修改标题
admin.site.site_title="后台管理系统"
#修改网站头部
admin.site.site_header="后台管理"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #设置后台显示的字段
    list_display = ["pk","name","weight","height","type"]
    a.colored_type.short_description = "带颜色的产品类型"
    #设置可以搜索的字段
    search_fields = ['name','type__type_name']
    #设置过滤器
    list_filter = ['type__type_name']
    #设置排序方式,默认是正序，-pk 表示倒序
    ordering = ['pk']

    #重写get_readonly_files函数设置超级用户的权限
    def get_readonly_files(self,request,obj=None):
        if request.user.is_superuser:
            self.readonly_fields=[]
        return self.readonly_fields

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["pk","type_name"]
    search_fields = ['type_name']
    ordering = ["pk"]


