from django.shortcuts import render,redirect
from .form import *
from django.http import HttpResponse

#数据表单的使用
def model_index(request):
    pass

def index(request):
    #get请求
    if request.method=='GET':
        product=ProductForm()
        return render(request,'data_form.html',locals())
    #post请求
    else:
        product=ProductForm(request.POST)
        if product.is_valid():
            #获取网页空间name数据
            name=product['name']
            cname=product.cleaned_data['name']
            return HttpResponse('提交成功')
        else:
            #输出错误信息
            error_msg=product.errors.as_json()
            print(error_msg)
            return render(request,'data_form.html',locals())


'''
# Create your views here.
import csv
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("django重定向")
    #return render(request,'index.html',context={'title':'首页'},status=500)


def mydate(request,year,month,day):
    return HttpResponse(str(year)+"/"+str(month)+"/"+str(day))

#变量url
def myyear(request,year):
    return render(request,'myyear.html')

#文件下载
def download(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="somefilename.csv"'
    writer=csv.writer(response)
    writer.writerow(['First row','A','B','C'])
    return response

#重定向
from django.shortcuts import redirect
def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        return redirect('/')
    else:
        if request.GET.get('name'):
            name=request.GET.get('name')
        else:
            name='Everyone'
    return HttpResponse('username is'+name)

#数据可视化
from .models import Product
def index(request):
    #type_list=Product.objects.values("type").distinct()
    type_list=Product.objects.all().distinct()
    name_list=Product.objects.values("name","type")
    context={'title':'首页','type_list':type_list,'name_list':name_list}
    return render(request,'index1.html',context=context)

#通用视图
from django.views.generic import ListView
class ProductList(ListView):
    context_object_name = 'type_list'
    template_name = 'index1.html'
    queryset = Product.objects.values('type').distinct()

    def get_queryset(self):
        type_list=Product.objects.values('type').distinct()
        return type_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(ProductList, self).get_context_data(**kwargs)
        context['name_list']=Product.objects.values('name','type')
        return context

#查询数据测试
def test(request):
    c=Product.objects.all()
    return HttpResponse(c)

'''

