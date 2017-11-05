#coding=utf-8
from django.contrib import admin
from models import *
# Register your models here.
class ToolTypeAdmin(admin.ModelAdmin):
    list_display=('id','type_name')
admin.site.register(ToolType,ToolTypeAdmin)

class ToolAdmin(admin.ModelAdmin):
    list_display=('id','Name','Description','Size','Link','Type','Instructions','Time')
admin.site.register(Tool,ToolAdmin)


