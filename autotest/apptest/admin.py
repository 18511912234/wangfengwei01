from django.contrib import admin
from apptest.models import *
# Register your models here.

class AppcasestepAdmin(admin.TabularInline):
    list_display=['id','appteststep','apptestobjname','appfindmethod','appevelement','appoptmethod','appassertdata','apptestresult','create_time','appcase']
    model = Appcasestep
    extra = 1

class AppcaseAdmin(admin.ModelAdmin):
    list_display = ['id','appcasename','apptestresult','create_time']
    inlines = [AppcasestepAdmin]

admin.site.register(Appcase,AppcaseAdmin)


