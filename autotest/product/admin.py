from django.contrib import admin
from apptest.models import Appcase
from webtest.models import Webcase
# Register your models here.

from product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','productname','productdescription','producter','create_time']
    search_fields = ['productname']
    ordering = ['id']
    list_per_page = 10

#app自动化用例管理
class AppcaseAdmin(admin.TabularInline):
    list_display = ['id','appcasename','apptestresult','create_time','product']
    model = Appcase
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','productname','productdesc','create_time']
    inlines = [AppcaseAdmin]

#web自动化用例管理
class WebcaseAdmin(admin.TabularInline):
    list_display = ['id','webcasename','webtestresult','create_time','product']
    model = Webcase
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','productname','productdesc','create_time']
    inlines = [WebcaseAdmin]