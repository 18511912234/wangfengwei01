from . import views
from django.urls import path,include

urlpatterns=[
    path('login.html',views.loginView,name='login'),
    path('register.html',views.registerView,name='register'),
    path('setpassword.html',views.setpasswordView,name='setpassword'),
    path('logout.html',views.logoutView,name='logout'),

    #发送邮件的url
    path('findPassword.html',views.findPassword,name='findPassword'),
]

