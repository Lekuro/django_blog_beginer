from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return f'{new_slug}-{str(int(time()))}'


class BlogPost(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True,
                            blank=True)  # A-Za-z0-9-_
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('BlogTag', blank=True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost_detail_endpoint', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('blogpost_update_endpoint', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('blogpost_delete_endpoint', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # if not self.id:
        self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_pub']


class BlogTag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def save(self, *args, **kwargs):
        # if not self.id:
        self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'title: {self.title}, slug: {self.slug}.'

    def get_absolute_url(self):
        return reverse('tag_detail_endpoint', kwargs={'slug': self.slug})

    def get_update_url(self):
        print('self.slug1', self.slug)
        # return('<h1> Hello</h1>')
        return reverse('tag_update_endpoint', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_endpoint', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']
