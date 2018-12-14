"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin#导入admin功能模块
from django.urls import path,include#导入url编写模块

#这是一个集合，不能重复，每个元素代表一条url信息
urlpatterns = [
    path('admin/', admin.site.urls), #admin/ 代表127.0.0.1:8000/ admin.site.urls代表url的处理函数也就是司徒函数
    #配置
   # path('',include('index.urls')),#r'^'代表 127.0.0.1:8000  include('index.urls')代表把这个url分发给index应用下的urls.py处理
    #path('',include('user.urls'))
]
