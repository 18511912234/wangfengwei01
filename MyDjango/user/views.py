from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

def test(request):
    pass


def loginView(request):
    title="登陆"
    unit_2='/user/register.html'

    unit_2_name="立即注册"
    unit_1='/user/setpassword.html'

    unit_1_name="修改密码"
    if request.method=="POST":
        username=request.POST.get("username",'')
        password=request.POST.get('password','')
        if User.objects.filter(username=username):
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                return HttpResponseRedirect('/')
            else:
                tips="账号密码错误，请重新输入"
        else:
            tips="用户不存在，请先注册"
    return render(request,"user.html",locals())

def registerView(request):
    title = "注册"
    unit_2 = '/user/login.html'

    unit_2_name = "立即登陆"
    unit_1 = '/user/setpassword.html'

    unit_1_name = "修改密码"
    if request.method == "POST":
        username = request.POST.get("username", '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            tips = "用户已存在"
        else:
            user=User.objects.create_user(username=username,password=password)
            user.save()
            tips="注册成功，请登录"
    return render(request, "user.html", locals())

def setpasswordView(request):
    title = "修改密码"
    unit_2 = '/user/login.html'

    unit_2_name = "立即登陆"
    unit_1 = '/user/register.html'

    unit_1_name = "立即注册"
    new_password=True
    if request.method == "POST":
        username = request.POST.get("username", '')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')

        if User.objects.filter(username=username):
            user=authenticate(username=username,passowrd=old_password)
            user.set_password(new_password)
            user.save()
            tips="修改密码成功"
        else:
            tips="用户不存在"
    return render(request, "user.html", locals())

def setpasswordView_1(request):
    if request.method=="POST":
        username=request.POST.get("username",'')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        #user=User.objects.filter(username=username)
        if User.objects.filter(username=username):
            user=authenticate(username=username,passowrd=old_password)
            dj_ps=make_password(new_password,None,'pdkdf2_sha256')
            user.password=dj_ps
            user.save()
    return render(request, "user.html", locals())



def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/')

#发送邮件
import random
#找回密码
def findPassword(request):
    button="获取验证码"
    new_password=False
    if request.method=="POST":
        username=request.POST.get('username')
        VerificationCode=request.POST.get('VerificationCode')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)
        if not user:
            tips="用户"+username+"不存在"
        else:
            #判断验证码是否已发送
            if not request.session.get('VerificationCode'):
                button="重置密码"
                tips="验证码已发送"
                new_password=True
                VerificationCode=str(random.randint(1000,9999))
                VerificationCode=request.session['VerificationCode']
                user[0].email_user("找回密码",VerificationCode)
                #判断输入得验证码和发送得是否一致
            elif VerificationCode==request.session.get('VerificationCode'):
                dj_ps=make_password(password,None,'pbkdf2_sha256')
                dj_ps=user[0].password
                user[0].save()
                del request.session['VerificationCode']
                tips="密码已重置"
            else:
                tips='验证码错误，请重新输入'
                new_password=False
                del request.session['VerificationCode']
    return render(request,'user.html',locals())

