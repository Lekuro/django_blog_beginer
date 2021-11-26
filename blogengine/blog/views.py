from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from blog.models import BlogPost, BlogTag
from django.views.generic import View
from blog.utils import ObjectDetailMixin
from blog.forms import TagForm


def blogposts_list(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'blog/index.html', context={'blogposts': blogposts})


def tags_list(request):
    tags = BlogTag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class TagCreateView(View):
    def get(self, request):
        print(request)
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        print('dir(request)',dir(request))
        print('request.POST', request.POST)
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag=bound_form.save()
            return redirect(new_tag)
        return render(request,'blog/tag_create.html',context={'form':bound_form})


class BlogPostDetailView(ObjectDetailMixin, View):
    model = BlogPost
    template = 'blog/post_detail.html'


class TagDetailView(ObjectDetailMixin, View):
    model = BlogTag
    template = 'blog/tag_detail.html'

# class BlogPostDetailView(View):
#     def get(self, request, slug):
#         # post = BlogPost.objects.get(slug__iexact=slug)
#         post = get_object_or_404(BlogPost, slug__iexact=slug)
#         return render(request, 'blog/post_detail.html', context={'blogpost': post})


# class TagDetailView(View):
#     def get(self, request, slug):
#         # tag = BlogTag.objects.get(slug__iexact=slug)
#         tag = get_object_or_404(BlogTag, slug__iexact=slug)
#         return render(request, 'blog/tag_detail.html', context={'blogtag': tag})

# uncomment urls too
# def blogpost_detail(request, slug):
# #    post = BlogPost.objects.get(slug__iexact=slug)
#     post = get_object_or_404(BlogPost, slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'blogpost': post})

# def tag_detail(request, slug):
#     # tag = BlogTag.objects.get(slug__iexact=slug)
#     tag = get_object_or_404(BlogTag, slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'blogtag': tag})

def hello(request):
    print('request ', request)
    print('dir(request)')
    print(dir(request))
    return HttpResponse('<h1>Hello world</h1>')
