from django.apps import AppConfig
import os
from index import *

#定义一个函数获取应用的命名
def get_current_app_name(__file):
    return os.path.split(os.path.dirname(__file))[-1]

#重写类设置应用名字是 网站首页
class IndexConfig(AppConfig):
    name=get_current_app_name(__file__)
    verbose_name="网站首页"

