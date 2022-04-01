from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from .models import Post
from .models import Group
from .models import User

date = 10
number = 10


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, number)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.filter(group=group)
    paginator = Paginator(post_list, number)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    author = User.objects.get(username=username)
    post = author.post.select_related('group').all()
    post_count = post.count()
    paginator = Paginator(post, number)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'post': post,
        'page_obj': page_obj,
        'post_count': post_count,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    author = post.author
    posts_count = author.post.count()
    context = {
        'author': author,
        'post': post,
        'posts_count': posts_count,
    }
    return render(request, 'posts/post_detail.html', context)
