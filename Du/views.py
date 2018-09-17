from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
import markdown

# Create your views here.
# 首页
from django.views.generic import ListView, DetailView

from Du.forms import LoginForm, RegisterForm, CommentForm
from Du.models import News, Blog, Music, Comment


def index(request):
    blog_list = Blog.objects.all()
    return render(request, 'index.html', context={'blog_list': blog_list})

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

    def get_object(self, queryset=None):
        blog = super(blog_detail, self).get_object(queryset=None)
        blog.article = markdown.markdown(blog.article, extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc'])
        return blog

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        comment_list = Comment.objects.all()
        comment_form = CommentForm()
        context.update({
            'comment_list': comment_list,
            'comment_form': comment_form
        })
        return context


class music(ListView):
    model = Music
    template_name = 'music.html'
    context_object_name = 'music_list'


# 登录页面
def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Du:index')
            else:
                message = '您输入的用户名或密码错误，请重新输入'
                return render(request, 'login.html', {'form': login_form, 'message': message})
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'form': login_form})

# 注销页面
def logout_view(request):
    logout(request)
    return redirect('Du:index')


# 注册页面
def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        user = User()
        if register_form.is_valid():
            user.username = request.POST.get('username', '')
            user.email = request.POST.get('email', '')
            user.password = request.POST.get('password', '')
            user.save()
            return redirect('Du:index')
    else:
        register_form = RegisterForm()
    return render(request, 'register.html', {'form': register_form})

# 处理评论
def blog_comment(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    author = get_object_or_404(User)

    # 只有POST的时候才处理
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # 先关联，不保存
            comment = form.save(commit=False)
            # 关联博客数据
            comment.blog = blog
            # 关联评论数据
            comment.author = author
            # 保存到数据库
            comment.save()
            return redirect(blog)
        else:
            comment_list = blog.comment_set.all()
            context = {
                'blog': blog,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blog_detail.html', context=context)

    return redirect('Du:blog')


# sitemap页面
def get_sitemap(request):
    return render(request, 'sitemap.xml')

