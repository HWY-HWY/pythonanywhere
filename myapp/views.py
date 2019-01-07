from django.shortcuts import render
from myapp.models import Blog
from django.core.paginator import Paginator

# Create your views here.


# 首页
def index(request):
    # 得到当前所处的页数
    now_page_num = request.GET.get('page_num', 1)
    print(now_page_num)
    # 得到Blog的分页器
    paginator = create_page()
    # 得到具体的页数
    now_page = paginator.get_page(now_page_num)
    # 利用分页器判断当前页是否存在上一页
    is_previous_page = now_page.has_previous()
    # 判断当前页是否存在下一页
    is_next_page = now_page.has_next()
    # 得到所有的博客列表
    blog_list = Blog.objects.all().order_by('-pk')
    context = {}
    context['blog_list'] = blog_list
    context['page_num'] = int_become_list(paginator.num_pages, int(now_page_num))
    context['now_page_num'] = int(now_page_num)
    context['is_previous_page'] = is_previous_page
    context['is_next_page'] = is_next_page
    return render(request, 'index.html', context)


# 整型数据转化为list
def int_become_list(num, now_page_num):
    num_list = []
    for i in range(num):
        num_list.append(i + 1)
    if now_page_num - 2 > 0:
        num_list = num_list[now_page_num - 2:]
    print(num_list)
    return num_list


# 该函数用于对Blog中的文章进行分页
def create_page():
    # 获得所有的文章
    blog_list = Blog.objects.all()
    # 使用django分页器进行分页，分页基数为1
    paginator = Paginator(blog_list, 1)
    return paginator


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
