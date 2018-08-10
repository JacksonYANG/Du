from django.conf.urls import url

from Du import views

app_name = 'Du'

urlpatterns = [
    # 首页匹配
    url(r'^$', views.index, name='index'),

    # 热点匹配
    url(r'^hot/$', views.hot.as_view(), name='hot'),

    # 热点详细
    url(r'^hot_detail/(?P<pk>[0-9]+)/$', views.hot_detail.as_view(), name='hot_detail'),

    # 博客页面匹配
    url(r'^blog/$', views.blog.as_view(), name='blog'),

    # 详细页面匹配
    url(r'^detail/(?P<pk>[0-9]+)/$', views.blog_detail.as_view(), name='detail'),

    # 个人账户页面匹配
    url(r'^user/$', views.user, name='user'),

]