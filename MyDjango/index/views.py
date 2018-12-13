from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("简单的流程测试")

def mydate(request,year,month,day):
    return HttpResponse(str(year)+"/"+str(month)+"/"+str(day))

def myyear(request):
    return render(request,'myyear.html')
