from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.rankingView, name='ranking'),
    # 通用视图
    re_path(r'^list/$', views.RankingList.as_view(), name='rankingList'),
]