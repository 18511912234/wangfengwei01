from django.contrib import admin
from set.models import Set
# Register your models here.

@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ['id','setname','setvalue']
    ordering = ['id']
