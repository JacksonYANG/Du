from django.shortcuts import render

# Create your views here.
# 首页
from django.views.generic import ListView,DetailView

from Du.models import News, Blog


def index(request):
    return render(request, 'index.html')

# 热点页面
class hot(ListView):
    model = News
    template_name = 'hot.html'
    context_object_name = 'news_list'


# 热点详细页面
class hot_detail(DetailView):
    model = News
    template_name = 'hot_detail.html'
    context_object_name = 'news_detail'

    def get(self, request, *args, **kwargs):
        response = super(hot_detail, self).get(request, *args, **kwargs)
        self.object.increase_browse()
        return response

# 博客页面
class blog(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog_list'

# 详细页面
class blog_detail(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog_detail'

    def get(self, request, *args, **kwargs):
        response = super(blog_detail, self).get(request, *args, **kwargs)
        self.object.increase_browse()
        return response


# 个人页面
def user(request):
    return render(request, 'me.html')