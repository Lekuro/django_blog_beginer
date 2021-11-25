from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogPost

def hello(request):
    print('request ', request)
    print('dir(request)')
    print(dir(request))
    return HttpResponse('<h1>Hello world</h1>')

def blogposts_list(request):
    blogposts = BlogPost.objects.all()
    return render(request,'blog/index.html', context={'blogposts':blogposts})

def blogpost_detail(request,slug):
    post= BlogPost.objects.get(slug__iexact=slug)
    print(request,post)
    return render(request,'blog/post_detail.html',context={'blogpost':post})
