from django.db import models

from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    # 标题，内容，浏览次数，创建日期，修改日期, 作者
    title = models.CharField(max_length=20)
    article = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    browse = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    # 浏览次数自动增加
    def increase_browse(self):
        self.browse +=1
        self.save(update_fields=['browse'])

    # 详情页的时候打开详细内容
    def get_absolute_url(self):
        return reverse('Du:detail', kwargs={'pk': self.pk})

class Music(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    source = models.CharField(max_length=255)

# 热点数据库
class Category(models.Model):
    name = models.CharField(max_length=10)

class News(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    source = models.CharField(max_length=10)
    date = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    browse = models.PositiveIntegerField(default=0)

    # 浏览次数自动增加
    def increase_browse(self):
        self.browse += 1
        self.save(update_fields=['browse'])

    # 详情页的时候打开详细内容
    def get_absolute_url(self):
        return reverse('Du:hot_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    # 用户名
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:20]




