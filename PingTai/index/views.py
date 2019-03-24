from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from index.models import *
# Create your views here.
from index.models import *
from index import util

def index(request):
    students = Users.objects.all()
    return render(request, 'index.html', {'students': students, 'flag': 1})


def home(request):
    user = request.GET.get('user')
    return render(request, 'home.html', {'username': user})

def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def api_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        if Users.objects.filter(username=username, password=password).exists():
            return JsonResponse({"flag": 1, "username": username})
        else:
            return JsonResponse({"flag": 0, "msg": '用户名或密码错误'})
    else:
        return JsonResponse({"flag": 0, 'msg': '缺少必填参数：username or password'})

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

def user_exist(request):
    username = request.POST.get('username')
    if username:
        if Users.objects.filter(username=username).exists():
            return JsonResponse({'flag': 0})
        else:
            return JsonResponse({'flag': 1})
    else:
        return JsonResponse({'flag': 2})

def task(request):
    tasks = Task.objects.all().order_by('-id')
    cases = Cases.objects.all().order_by('-id')
    return render(request, 'task.html', {"tasks": tasks, "cases": cases})

def task_search(request):
    name = request.POST.get('name')
    print(name)
    if name:
        tasks = Task.objects.filter(name__contains=name)
    else:
        tasks = Task.objects.all()
    task_list = []
    for task in tasks:
        task_list.append({"id": task.id, "name": task.name})
    return JsonResponse({"tasks": task_list} )


def new_task(request):
    name = request.POST.get('name')
    desc = request.POST.get('desc')
    cases =  request.POST.get('cases')
    cases_list = cases.split(",")
    if name and cases:
        if not Task.objects.filter(name=name).exists():
            task = Task.objects.create(name=name, description=desc)
            for case_id in cases_list:
                case = Cases.objects.filter(id=case_id).first()
                task.cases.add(case)
            flag = 0
        else:
            flag = 1
    else:
        flag = 2
    return JsonResponse({"flag": flag})

def delete_task(request):
    id = request.POST.get('id')
    task = Task.objects.filter(id=id).first()
    if task:
        task.delete()
        flag = 1
    else:
        flag = 0
    return JsonResponse({"flag": flag})

def get_task(request):
    id = request.POST.get('id')
    task = Task.objects.filter(id=id).first()
    if task:
        result = {"flag":1, "id":task.id, "name": task.name, "desc": task.description}
    else:
        result = {"flag": 0}
    return JsonResponse(result)

def case_new(request):
    return render(request, 'case_new.html')

def case_list(request):
    cases = Cases.objects.all().order_by('-id')
    return render(request, 'case_list.html', {"cases": cases})

def api_case_new(request):
    name = request.POST.get('name')
    method = request.POST.get('method')
    desc = request.POST.get('desc')
    url = request.POST.get('url')
    head_key = request.POST.getlist('head_key')
    head_value = request.POST.getlist('head_value')
    body_type = request.POST.get('body_type')
    body_value = request.POST.get('body_value')
    check_type = request.POST.getlist('check_type')
    check_value = request.POST.getlist('check_value')
    if name and method and url and body_type and check_type and check_value:
        #拼接头信息
        headers_list = []
        if head_key and head_value:
            for i in range(0, len(head_key)):
                if head_key[i] and head_value[i]:
                    headers_list.append(head_key[i]+'='+head_value[i])

        # 拼接检查点信息
        check_list = []
        if check_type and check_value:
            for i in range(0, len(check_type)):
                if check_type[i] and check_value[i]:
                    check_list.append(check_type[i]+'='+check_value[i])
        #入库
        try:
            Cases.objects.create(name=name, desc=desc, method=method, url=url,
                                 headers='&'.join(headers_list),body_type=body_type,
                                 body_value=body_value, checks='&'.join(check_list))
            return HttpResponseRedirect('/index/case_list/')
        except:
            return render(request, 'error.html', {'msg': '新增用例失败'})
    else:
        return render(request, 'error.html', {'msg': '用例缺少必填参数'})

    return render(request, 'case_new.html')


def api_run(request):
    flag = 1
    report_url = ''
    tid = request.POST.get("tid")
    task = Task.objects.filter(id=tid).first()
    if task:
        #取到task关联的每个用例的详细信息
        case_list = []
        for case in task.cases.all():
            data = {}
            data['id'] = case.id
            data['name'] = case.name
            data['desc'] = case.desc
            data['method'] = case.method
            data['url'] = case.url
            data['headers'] = case.headers
            data['body_type'] = case.body_type
            data['body_value'] = case.body_value
            data['checks'] = case.checks
            case_list.append(data)
        report_url = util.start_run(case_list)
        flag = 0
    return JsonResponse({"flag": flag, "report": report_url})