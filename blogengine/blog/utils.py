from django.shortcuts import render, redirect, get_object_or_404
from blog.models import BlogPost, BlogTag


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        # obj = BlogPost.objects.get(slug__iexact=slug)
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template,
                      context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        # print(request)
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        # print('dir(request)', dir(request))
        # print('request.POST', request.POST)
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        print('request', request)
        print('slug', slug)
        print('model name',self.model.__name__.lower())
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):
        print('request', request)
        print('slug', slug)
        print('model name',self.model.__name__.lower())
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            edited_obj = bound_form.save()
            return redirect(edited_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})
