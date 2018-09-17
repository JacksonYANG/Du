from django.conf.urls import url
from django.contrib.admin import register
from django.contrib.auth import login, logout

from Du import views

app_name = 'Du'

urlpatterns = [
    # 首页匹配
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),

    # 热点匹配
    url(r'^hot/$', views.hot.as_view(), name='hot'),

    # 热点详细
    url(r'^hot_detail/(?P<pk>[0-9]+)/$', views.hot_detail.as_view(), name='hot_detail'),

    # 博客页面匹配
    url(r'^blog/$', views.blog.as_view(), name='blog'),

    # 博客评论页面
    url(r'^blog/(?P<blog_pk>[0-9]+)/comment/$', views.blog_comment, name = 'blog_comment'),

    # 详细页面匹配
    url(r'^blog_detail/(?P<pk>[0-9]+)/$', views.blog_detail.as_view(), name='detail'),

    # 后续提供音乐服务
    url(r'^music/$', views.music.as_view(), name='music'),

    # 登录页面匹配
    url(r'^login/$', views.login_view, name='login'),

    # 注册页面匹配
    url(r'^register/$', views.register, name='register'),

    # 注销页面
    url(r'^logout/$', views.logout_view, name='logout'),

    # 匹配sitemap
    url(r'^sitemap.xml$', views.get_sitemap, name='sitemap')


]