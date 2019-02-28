from django.contrib import admin
from .models import Apitest,Apistep,Apis
from product.models import Product
# Register your models here.

#在ApitestAdmin页面可以编辑ApistepAdmin
class ApistepAdmin(admin.TabularInline):
    list_display=['id','apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','apitest']
    model = Apistep
    extra = 1

@admin.register(Apitest)
class ApitestAdmin(admin.ModelAdmin):
    list_display = ['id','apitestname','apitester','apitestresult','create_time']
    inlines = [ApistepAdmin]


class ApisAdmin(admin.TabularInline):
    list_display=['id','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','product','apiname']
    model = Apis
    extra = 1
admin.site.register(Apis)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','productname','productdesc','create_time']
    inlines = [ApisAdmin]

