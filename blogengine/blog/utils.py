from django.shortcuts import render, get_object_or_404
from blog.models import BlogPost, BlogTag

class ObjectDetailMixin:
    model=None
    template=None
    def get(self, request, slug):
        # obj = BlogPost.objects.get(slug__iexact=slug)
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, 
        context={self.model.__name__.lower(): obj})
