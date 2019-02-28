from django.shortcuts import render
from product.models import Product
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

#产品管理+分页
def product_manage(request):
    username=request.session.get("user")
    product_list=Product.objects.all()
    paginator = Paginator(product_list, 10)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        product_list = paginator.page(paginator.num_pages)
    product_count=Product.objects.all().count()
    return render(request,"product_manage.html",{"user":username,"products":product_list,"productcounts":product_count})

#搜索
def productsearch(request):
    username=request.session.get("user")
    search_productname=request.GET.get("productname")
    product_list=Product.objects.filter(productname_icontains=search_productname)
    return render(request,'product_manage.html',{"user":username,"apitests":product_list})