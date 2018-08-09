from django.db import models

from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    # 标题，内容，浏览次数，创建日期，修改日期, 作者
    title = models.CharField(max_length=20)
    article = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    browse = models.PositiveIntegerField(default=0)

    # 浏览次数自动增加
    def increase_browse(self):
        self.browse +=1
        self.save(update_fields=['browse'])

    # 详情页的时候打开详细内容
    def get_absolute_url(self):
        pass

# 作者的信息
class Author(models.Model):
    name = models.CharField(max_length=20)
    

