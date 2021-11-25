from django.db import models
from django.shortcuts import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)  # A-Za-z0-9-_
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost_detail_endpoint', kwargs={'slug': self.slug})
