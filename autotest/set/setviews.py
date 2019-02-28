from django.shortcuts import render
from set.models import Set
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

#系统管理+分页
def set_manage(request):
    username=request.session.get('user')
    set_list=Set.objects.all()
    paginator = Paginator(set_list, 10)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        set_list = paginator.page(page)
    except PageNotAnInteger:
        set_list = paginator.page(1)
    except EmptyPage:
        set_list = paginator.page(paginator.num_pages)

    return render(request,'set_manage.html',{"user":username,"sets":set_list})

#用户管理
def set_user(request):
    user_list=User.objects.all()
    username=request.session.get('user')
    return render(request,'set_user.html',{'user':username,'users':user_list})

#搜索
def setsearch(request):
    username=request.session.get("user")
    search_setname=request.GET.get("setname")
    set_list=Set.objects.filter(setname__icontains=search_setname)
    return render(request,'set_manage.html',{"user":username,"apitests":set_list})

#用户搜索
def usersearch(request):
    username=request.session.get("user")
    search_username=request.GET.get("username")
    user_list=User.objects.filter(username__icontains=search_username)
    return render(request,'set_user.html',{"user":username,"usernames":user_list})
