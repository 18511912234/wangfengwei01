from django.contrib import admin

# Register your models here.
from bug.models import Bug

@admin.register(Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ['id','bugname','bugdetail','bugstatus','buglevel','bugcreater','bugassign','create_time']
