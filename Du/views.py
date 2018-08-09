from django.shortcuts import render

# Create your views here.
# 首页
from django.views.generic import ListView,DetailView


def index(request):
    pass

# 博客页面
class blog(ListView):
    pass

# 详细页面
class detail(DetailView):
    pass

# 个人页面
def user(request):
    pass