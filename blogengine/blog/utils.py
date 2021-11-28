from django.shortcuts import render, redirect, get_object_or_404
from blog.models import BlogPost, BlogTag

class ObjectDetailMixin:
    model=None
    template=None
    def get(self, request, slug):
        # obj = BlogPost.objects.get(slug__iexact=slug)
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, 
        context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    form_model=None
    template=None

    def get(self, request):
        print(request)
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        print('dir(request)', dir(request))
        print('request.POST', request.POST)
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form': bound_form})