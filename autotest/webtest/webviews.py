from django.shortcuts import render
from webtest.models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
#用例管理
def webcase_manage(request):
    webcase_list=Webcase.objects.all()
    username=request.session.get('user')
    paginator = Paginator(webcase_list, 10)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        webcase_list = paginator.page(page)
    except PageNotAnInteger:
        webcase_list = paginator.page(1)
    except EmptyPage:
        webcase_list = paginator.page(paginator.num_pages)
    webtest_count = Webcase.objects.all().count()
    return render(request,'webcase_manage.html',{'user':username,'webcases':webcase_list,"webcasecounts":webtest_count})

#用例测试步骤
def webcasestep_manage(request):
    username = request.session.get('user')
    webcasestep_list=Webcasestep.objects.all()
    paginator = Paginator(webcasestep_list, 10)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        webcasestep_list = paginator.page(page)
    except PageNotAnInteger:
        webcasestep_list = paginator.page(1)
    except EmptyPage:
        webcasestep_list = paginator.page(paginator.num_pages)
    return render(request,'webcasestep_manage.html',{'user':username,'webcasesteps':webcasestep_list})


#webcase搜索
def websearch(request):
    username=request.session.get("user")
    search_webcasename=request.GET.get("webcasename")
    webcase_list=Webcase.objects.filter(webcasename__icontains=search_webcasename)
    return render(request,'webcase_manage.html',{"user":username,"webcases":webcase_list})

#webcasestep搜索
def websetpsearch(request):
    username=request.session.get("user")
    search_webstepname=request.GET.get("webcasestepname")
    webstep_list=Webcasestep.objects.filter(webstepname__icontains=search_webstepname)
    return render(request,'webcasestep_manage.html',{"user":username,"webcasesteps":webstep_list})
