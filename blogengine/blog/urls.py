from django.urls import path
from blog.views import *

urlpatterns = [
    path('hello/', hello),
    path('blogposts/', blogposts_list, name='blogpost_list_endpoint'),
    path('blogpost/<str:slug>/', blogpost_detail,
         name='blogpost_detail_endpoint'),
    path('tags/', tags_list, name='tags_list_endpoint'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail_endpoint'),
]
