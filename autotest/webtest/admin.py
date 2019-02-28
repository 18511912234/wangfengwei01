from django.contrib import admin
from webtest.models import *
# Register your models here.

class WebcasestepAdmin(admin.TabularInline):
    list_display=['id','webcasename','webteststep','webtestobjname','webfindmethod','webevelement','weboptmethod','webassertdata','webtestresult','create_time','webcase']
    model = Webcasestep
    extra = 1

class WebcaseAdmin(admin.ModelAdmin):
    list_display = ['id','webcasename','webtestresult','create_time']
    inlines = [WebcasestepAdmin]

admin.site.register(Webcase,WebcaseAdmin)
