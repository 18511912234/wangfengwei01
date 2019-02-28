from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import *
# Create your views here.

def index(request):
    return render(request,"index.html")

#登陆
def login(request):
    return render(request, 'login.html')

#注册
def register(request):
    return render(request,'register.html')

# #登陆后的页面
# def api_login(request):
#     username=request.POST.get("username")
#     password=request.POST.get("password")
#     if username and password:
#         if Users.objects.filter(username=username,password=password).exists():
#             return render(request,"home.html",{"username":username})
#         else:
#             return render(request, "error.html",{"msg":"用户名或密码错误"})
#     else:
#         return render(request,"error.html",{"msg":"必填参数密不能为空"})
#
# #注册后页面
# def api_register(request):
#     username = request.POST.get("username")
#     password = request.POST.get("password")
#     #password1 = request.POST.get("password1")
#     email=request.POST.get("email")
#     if username and password and email:
#         if not Users.objects.filter(username=username).exists():
#             try:
#                 Users.objects.create(username=username, password=password, email=email)
#                 return  HttpResponseRedirect("/index/login/")
#             except:
#                 return render(request, "error.html", {"msg": "数据库未知错误"})
#         else:
#             return render(request, "error.html", {"msg": "用户名已存在"})
#     else:
#         return render(request,"error.html",{"msg":"必填参数不能为空"})


def home(request):
    user=request.GET.get("username")
    return render(request,"home.html")

def api_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        if Users.objects.filter(username=username, password=password).exists():
            #return render(request, 'home.html', {'username': username})
            return JsonResponse({"flag":1,"username":username})
        else:
            #return render(request, 'error.html', {'msg': '用户名或密码错误'})
            return JsonResponse({"flag":0,"username":username})

    else:
        return render(request, 'error.html', {'msg': '缺少必填参数：username or password'})

def api_register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    if username and password and email:
        if not Users.objects.filter(username=username).exists():
            try:
                Users.objects.create(username=username, password=password, email=email)
                return HttpResponseRedirect('/index/login/')
            except:
                return render(request, 'error.html', {'msg': '数据库错误'})
        else:
            return render(request, 'error.html', {'msg': '用户名已存在'})
    else:
        return render(request, 'error.html', {'msg': '缺少必填参数：username or password'})

#判断用户名是否存在的接口
def user_exist(request):
    username=request.POST.get('username')
    if username:
        if Users.objects.filter(username=username).exists():
            return JsonResponse({"flag":0})
        else:
            return JsonResponse({"flag":1})
    else:
        return JsonResponse({"flag":2})
