from django.contrib import admin
from myapp.models import Blog

# Register your models here.

# 定义过滤器
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'author', 'blog_type')

admin.site.register(Blog, BlogAdmin)
