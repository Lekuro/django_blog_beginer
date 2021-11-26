from django import forms
from django.forms import widgets
from blog.models import *
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    # bad way write forms based on forms.Form
    # title = forms.CharField(max_length=50)
    # slug = forms.CharField(max_length=50)

    # title.widget.attrs.update({'class':'form-control'})
    # slug.widget.attrs.update({'class':'form-control'})

    class Meta:
        model = BlogTag
        fields = ['title', 'slug']  # '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        # new_slug=self.cleaned_data['slug'] # here good but in another clean_title no
        new_slug = self.cleaned_data.get('slug').lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create" or "create"')
        if BlogTag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(
                f'Slug must be unique. We have "{new_slug}".')
        return new_slug

    # for: forms.Form
    # def save(self):
    #     new_tag = BlogTag.objects.create(
    #         title=self.cleaned_data['title'],
    #         slug=self.cleaned_data['slug']
    #     )
    #     return new_tag


