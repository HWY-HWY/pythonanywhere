from django.shortcuts import render
from myapp.models import Blog

# Create your views here.

# 首页
def index(request):
    # 得到所有的博客列表
    blog_list = Blog.objects.all().order_by('-pk')
    context = {'blog_list': blog_list}
    return render(request, 'index.html', context)

# 博客内容页
def content(request):
    # 得到查询文章的pk
    pk = request.GET.get('pk')
    # 得到查询的类型
    request_type = request.GET.get('type')
    # 查询下一篇博客
    if request_type == 'next':
        pk = str(int(pk) + 1)
    # 查询上一篇博客
    elif request_type == 'previous':
        pk = str(int(pk) - 1)
    # 正常查询
    else:
        pk = pk
    # 判断该篇博客是否存在
    blog_status = Blog.objects.filter(pk=pk).exists()
    # 定义返回的数据集
    context = {}
    context['blog_status'] = blog_status
    # 存在该篇博客，返回博客数据并判断是否存在上一页、下一页
    if blog_status:
        # 判断是否存在下一篇博客
        next_page = Blog.objects.filter(pk=(str(int(pk) + 1))).exists()
        # 判断是否存在上一篇博客
        previous_page = Blog.objects.filter(pk=(str(int(pk) - 1))).exists()
        context['next_page'] = next_page
        context['previous_page'] = previous_page
        context['blog'] = Blog.objects.get(pk=pk)
    # 不存在则返回提示信息
    else:
        context['none_message'] = '没有查询到对应的博客'
    return render(request, 'content.html', context)

# 站点简介页面
def information(request):
    return render(request, 'information.html')
