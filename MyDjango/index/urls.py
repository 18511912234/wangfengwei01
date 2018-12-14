from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.index),
    path('<int:id>.html',views.model_index)
]

'''
    上面是带变量的url,添加带有字符类型，整形，slug的url
    说明：
    1.url中使用变量符号<>可以为url设置变量
    2.在它里面以冒号划分为两部分：前面代表变量的数据类型，后面代表变量名，变量名可自定义
    3.上面对新增的url设置了三个变量值：<year> 数据格式为字符型，<int:month> 数据格式为整形，<slug:day 数据格式为slug>


urlpatterns = [
    #path('index1',views.index),
    #带变量的url
    path('<year>/<int:month>/<slug:day>',views.mydate),
    #re_path是正则模块
    #?P是固定格式，要注意最后要加上斜杠或者其他字符，否则匹配不到
    #re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html',views.mydate)

    #url设置参数name
    re_path('^(?P<year>[0-9]{4})/$',views.myyear,name='myyear'),

    #重定向
    path('login',views.login),

    #文件下载
    path(r'download',views.download),

    #通用视图
    path('ProductList/',views.ProductList.as_view()),

    #查询测试
    path('test/',views.test)

]

'''