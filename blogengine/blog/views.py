from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogPost, BlogTag


def hello(request):
    print('request ', request)
    print('dir(request)')
    print(dir(request))
    return HttpResponse('<h1>Hello world</h1>')


def blogposts_list(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'blog/index.html', context={'blogposts': blogposts})


def blogpost_detail(request, slug):
    post = BlogPost.objects.get(slug__iexact=slug)
    print(request, post)
    return render(request, 'blog/post_detail.html', context={'blogpost': post})


def tags_list(request):
    tags = BlogTag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


def tag_detail(request, slug):
    tag = BlogTag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag})
