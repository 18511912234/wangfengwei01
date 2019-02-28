from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from apptest.models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

#用例管理
def appcase_manage(request):
    appcase_list=Appcase.objects.all()
    username=request.session.get('user')
    paginator = Paginator(appcase_list, 10)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        appcase_list = paginator.page(page)
    except PageNotAnInteger:
        appcase_list=paginator.page(1)
    except EmptyPage:
        appcase_list = paginator.page(paginator.num_pages)
    return render(request,'appcase_manage.html',{'user':username,'appcases':appcase_list})

#用例测试步骤
def appcasestep_manage(request):
    username = request.session.get('user')
    appcasestep_list=Appcasestep.objects.all()
    paginator = Paginator(appcasestep_list, 10)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        appcasestep_list = paginator.page(page)
    except PageNotAnInteger:
        appcasestep_list=paginator.page(1)
    except EmptyPage:
        appcasestep_list = paginator.page(paginator.num_pages)
    appcase_count = Appcase.objects.all().count()
    return render(request,'appcasestep_manage.html',{'user':username,'appcasesteps':appcasestep_list,"appcasecounts":appcase_count})

#app测试报告
def apptest_report(request):
    username=request.session.get('user')
    return render(request,"apptest_report.html",{"user":username})


#appcase搜索
def appsearch(request):
    username=request.session.get("user")
    search_appcasename=request.GET.get("appcasename")
    appcase_list=Appcase.objects.filter(appcasename__icontains=search_appcasename)
    return render(request,'appcase_manage.html',{"user":username,"appcases":appcase_list})

#appcasestep搜索
def appsetpsearch(request):
    username=request.session.get("user")
    search_appstepname=request.GET.get("appcasestepname")
    appstep_list=Appcasestep.objects.filter(appstepname__icontains=search_appstepname)
    return render(request,'appcasestep_manage.html',{"user":username,"appcasesteps":appstep_list})