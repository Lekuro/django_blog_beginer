from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from blog.models import BlogPost, BlogTag
from django.views.generic import View
from blog.utils import *
from blog.forms import TagForm, BlogPostForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


def blogposts_list(request):
    blogposts = BlogPost.objects.all()
    paginator = Paginator(blogposts, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
        print('prev_url',prev_url)
    else:
        prev_url = ''
    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
        print('next_url',next_url)
    else:
        next_url = ''
    context = {'page_obj': page,
               'is_paginated': is_paginated,
               'next_url': next_url,
               'prev_url': prev_url}
    # return render(request, 'blog/index.html', context={'blogposts': page.object_list})
    return render(request, 'blog/index.html', context=context)


def tags_list(request):
    tags = BlogTag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class BlogPostDeleteView(ObjectDeleteMixin,View):
    model = BlogPost
    template = 'blog/post_delete.html'
    redirect_url = 'blogposts_list_endpoint'

# class BlogPostDeleteView(LoginRequiredMixin, View):
#     raise_exception = True

#     def get(self, request, slug):
#         # post = BlogPost.objects.get(slug__iexact=slug)
#         post = get_object_or_404(BlogPost, slug__iexact=slug)
#         return render(request, 'blog/post_delete.html', context={'blogpost': post})

#     def post(self, request, slug):
#         post = BlogPost.objects.get(slug__iexact=slug)
#         post.delete()
#         return redirect(reverse('blogposts_list_endpoint'))


class TagDeleteView(ObjectDeleteMixin, View):
    model = BlogTag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_endpoint'


# class TagDeleteView(LoginRequiredMixin, View):
#     raise_exception = True

#     def get(self, request, slug):
#         tag = BlogTag.objects.get(slug__iexact=slug)
#         return render(request, 'blog/tag_delete.html', context={'tag': tag})

#     def post(self, request, slug):
#         tag = BlogTag.objects.get(slug__iexact=slug)
#         tag.delete()
#         return redirect(reverse('tags_list_endpoint'))


class BlogPostUpdateView(LoginRequiredMixin, ObjectUpdateMixin, View):
    raise_exception = True
    model = BlogPost
    model_form = BlogPostForm
    template = 'blog/post_update.html'


class TagUpdateView(LoginRequiredMixin, ObjectUpdateMixin, View):
    raise_exception = True
    model = BlogTag
    model_form = TagForm
    template = 'blog/tag_update.html'


# class TagUpdateView(LoginRequiredMixin, View):
#     raise_exception = True

#     def get(self, request, slug):
#         tag = BlogTag.objects.get(slug__iexact=slug)
#         bound_form = TagForm(instance=tag)
#         return render(request, 'blog/tag_update.html', context={'form': bound_form, 'tag': tag})

#     def post(self, request, slug):
#         tag = BlogTag.objects.get(slug__iexact=slug)
#         bound_form = TagForm(request.POST, instance=tag)

#         if bound_form.is_valid():
#             edited_tag = bound_form.save()
#             return redirect(edited_tag)
#         return render(request, 'blog/tag_update.html', context={'form': bound_form, 'tag': tag})


class BlogPostCreateView(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = BlogPostForm
    template = 'blog/post_create.html'
    raise_exception = True

    # def get(self, request):
    #     form = BlogPostForm()
    #     return render(request, 'blog/post_create.html', context={'form': form})

    # def post(self, request):
    #     bound_form = BlogPostForm(request.POST)
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'blog/post_create.html', context={'form': bound_form})


class TagCreateView(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True

    # def get(self, request):
    #     print(request)
    #     form = TagForm()
    #     return render(request, 'blog/tag_create.html', context={'form': form})

    # def post(self, request):
    #     print('dir(request)', dir(request))
    #     print('request.POST', request.POST)
    #     bound_form = TagForm(request.POST)
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_create.html', context={'form': bound_form})


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
