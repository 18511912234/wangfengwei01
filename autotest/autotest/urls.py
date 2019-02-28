from django.contrib import admin
from django.urls import path
from apitest import views
from product import proviews
from bug import bugviews
from set import setviews
from apptest import appviews
from webtest import webviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',views.test),
    path('login/',views.login),
    path('home/',views.home),
    path('logout/',views.logout),
    #产品管理
    path('product_manage/',proviews.product_manage),

    path('apitest_manage/',views.apitest_manage),
    path('apistep_manage/',views.apistep_manage),

    path('apis_manage/',views.apis_manage),

    #bug管理
    path('bug_manage/',bugviews.bug_manage),

    #系统管理
    path('set_manage/',setviews.set_manage),

    #用户管理
    path('user/',setviews.set_user),

    #app测试用例管理
    path('appcase_manage/',appviews.appcase_manage),
    path('appcasestep_manage/',appviews.appcasestep_manage),

    #app测试用例管理
    path('webcase_manage/',webviews.webcase_manage),
    path('webcasestep_manage/',webviews.webcasestep_manage),

    #测试报告
    path('test_report/',views.test_report),
    path("apptest_report/",appviews.apptest_report),

    #优化
    path('left/',views.left),

    #搜索
    path('apisearch/',views.apisearch),
    path('setsearch/',setviews.setsearch),
    path('productsearch/',proviews.productsearch),
    path('apissearch/',views.apisearch),
    path('bugsearch/',bugviews.bugsearch),
    path('appsearch/',appviews.appsearch),
    path('appstepsearch/',appviews.appsetpsearch),
    path('websearch/',webviews.websearch),
    path('webstepsearch/',webviews.websetpsearch),
    path('usersearch/',setviews.usersearch),

]
