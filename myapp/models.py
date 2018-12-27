from django.db import models

# Create your models here.

# 博客文章模型
class Blog(models.Model):
    # 指定标题字段
    title = models.CharField(max_length=100)
    # 指定日期字段
    date = models.DateField()
    # 指定作者字段
    author = models.CharField(max_length=50)
    # 指定类型字段
    blog_type = models.CharField(max_length=50)
    # 指定博客内容
    content = models.TextField()
