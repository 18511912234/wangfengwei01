"""PingTai URL Configuration

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
from django.contrib import admin
from django.urls import path
from index import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/home/', views.home),
    path('index/login/', views.login),
    path('index/register/', views.register),
    path('index/task/', views.task),
    path('api/login/', views.api_login),
    path('api/register/', views.api_register),
    path('api/user_exist/', views.user_exist),
    path('api/search_task/', views.task_search),
    path('api/new_task/', views.new_task),
    path('api/delete_task/', views.delete_task),
    path('api/get_task/', views.get_task),
    path('index/case_new/', views.case_new),
    path('index/case_list/', views.case_list),
    path('api/case_new/', views.api_case_new),
    path('api/run/', views.api_run)
]
