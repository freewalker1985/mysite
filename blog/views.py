from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post, Category, Tag, UserInfo
from .forms import UserInfoForm, LoginForm


# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'blog/post/list.html', {'posts': posts, 'page': page})

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/list.html'

def category_list(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = category.post_category.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def tag_list(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    posts = tag.post_tags.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def register(request):
    if request.session.get('is_login', None):
        return redirect('index')

    if request.method == 'POST':
        message = '请检查填写的内容'
        register_form = UserInfoForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password')
            password1 = register_form.cleaned_data.get('password1')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password != password1:
                message = '两次的密码不同'
                return render(request, 'blog/login/register.html', locals())
            else:
                same_user_name = UserInfo.objects.filter(username=username)
                if same_user_name:
                    message = '用户名已被使用'
                    return render(request, 'blog/login/register.html', locals())
                same_email = UserInfo.objects.filter(email=email)
                if same_email:
                    message = '邮箱已经被使用'
                    return render(request, 'blog/login/register.html', locals())

                new_user = UserInfo()
                new_user.username = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('/post_list/')

        else:
            return render(request, 'blog/login/register.html', locals())
    register_form = UserInfoForm()
    return render(request, 'blog/login/register.html', locals())


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        message = '清检查填写的内容'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = UserInfo.objects.get(username=username)
            except:
                message = '用户不存在'
                return render(request, 'blog/login/login.html', locals())
            if user.password == password:
                return redirect('/post_list/')
            else:
                message = '密码不正确'
                return render(request, 'blog/login/login.html', locals())
    login_form = LoginForm()
    return render(request, 'blog/login/login.html', locals())








