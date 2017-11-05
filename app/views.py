#coding=utf-8
from django.shortcuts import render,render_to_response,get_object_or_404,HttpResponse
from models import *
# Create your views here.
def GetTool(request,type_name_id):
    tools = Tool.objects.filter(Type__id=type_name_id)
    tooltype = get_object_or_404(ToolType,pk=type_name_id)
    types = ToolType.objects.all()
    return render_to_response('tool.html',{'tools':tools,'tooltype':tooltype,'types':types})
def GetType(request):
    types = ToolType.objects.all()
    return render_to_response('tool.html',{'types':types})
