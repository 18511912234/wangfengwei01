from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from .models import Apistep,Apitest,Apis
import pymysql
import HTMLTestReportCN
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
def test(request):
    return HttpResponse("hello test")

#登陆功能
def login(request):
    if request.POST:
        #username=password=''
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['user']=username
            response=HttpResponseRedirect('/home/')
            return response
        else:
            return render(request,'login.html',{'error':' 用户名或密码错误！'})
    return render(request,'login.html')

def home(request):
    return render(request,"home.html")
# 退出，
def logout(request):
    auth.logout(request)
    return render(request,'login.html')

#流程接口管理+分页功能
def apitest_manage(request):
    apitest_list=Apitest.objects.all()
    username=request.session.get("user")
    paginator=Paginator(apitest_list,10)
    page=request.GET.get('page',1)
    currentPage=int(page)
    try:
        apitest_list=paginator.page(page)
    except PageNotAnInteger:
        apitest_list=paginator.page(paginator.num_pages)
    apitest_count = Apitest.objects.all().count()
    return render(request,"apitest_manage.html",{"user":username,"apitests":apitest_list,"apitestcounts":apitest_count})

#接口步骤管理
#@login_required
def apistep_manage(request):
    username=request.session.get("user")
    apistep_list=Apistep.objects.all()
    paginator = Paginator(apistep_list, 10)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        apistep_list = paginator.page(page)
    except PageNotAnInteger:
        apistep_list = paginator.page(paginator.num_pages)
    return render(request,"apistep_manage.html",{"user":username,"apisteps":apistep_list})

#单一接口管理
def apis_manage(request):
    username=request.session.get('user')
    apis_list=Apis.objects.all()
    paginator = Paginator(apis_list, 10)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        apis_list = paginator.page(page)
    except PageNotAnInteger:
        apis_list = paginator.page(paginator.num_pages)

    apis_count = Apis.objects.all().count()
    return render(request,"apis_manage.html",{'user':username,'apiss':apis_list,"apiscounts":apis_count})

#测试报告
def test_report(request):
    username = request.session.get('user')
    apis_list = Apis.objects.all()
    apis_count=Apis.objects.all().count()#统计接口数量
    db=pymysql.connect(user='root',db='autotest',passwd='123456',host='127.0.0.1')
    cursor=db.cursor()
    sql1='select count(id) from apitest_apis where apitest_apis.apistatus=1'
    aa=cursor.execute(sql1)
    apis_pass_count=[row[0] for row in cursor.fetchmany(aa)][0]

    sql2='select count(id) from apitest_apis where apitest_apis.apistatus=0'
    bb=cursor.execute(sql2)

    apis_fail_count=[row[0] for row in cursor.fetchmany(bb)][0]
    db.close()

    return render(request,"report.html",{'user':username,"apiss":apis_list,"apiscounts":apis_count,
                                         "apis_pass_counts":apis_pass_count,"apis_fail_counts":apis_fail_count})

def left(request):
    return render(request,"left.html")

#搜索功能
def apisearch(request):
    username=request.session.get("user")
    search_apitestname=request.GET.get("apitestname")
    apitest_list=Apitest.objects.filter(apitestname__icontains=search_apitestname)
    return render(request,'apitest_manage.html',{"user":username,"apitests":apitest_list})



#搜索
def apissearch(request):
    username=request.session.get("user")
    search_apiname=request.GET.get("apiname")
    apis_list=Apis.objects.filter(apiname_icontains=search_apiname)
    return render(request,'apis_manage.html',{"user":username,"apiss":apis_list})