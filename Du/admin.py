from django.contrib import admin

# Register your models here.
from Du.models import Blog, News, Category, Comment, Music

admin.site.register(Blog)
admin.site.register(News)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Music)