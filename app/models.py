#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ToolType(models.Model):
    type_name=models.CharField(u'tooltype',max_length=32,unique=True)
    def __unicode__(self): 
        return self.type_name

class Tool(models.Model):  
    Name=models.CharField(u'工具名',max_length=100,unique=True)
    Description=models.TextField(u'简介',default='')
    Size=models.CharField(u'大小',max_length=200)
    Link=models.FileField(u'下载地址',upload_to='/toolbox/',default='')
    Type=models.ForeignKey(ToolType)
    Instructions=models.FileField(u'使用手册',upload_to='/tools/')
    Time=models.DateTimeField(u'更新时间',auto_now=True)
    def __unicode__(self): 
        return self.Name
