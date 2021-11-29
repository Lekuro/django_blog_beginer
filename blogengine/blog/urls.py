from django.urls import path
from blog.views import *

urlpatterns = [
    path('hello/', hello),
    path('blogposts/', blogposts_list, name='blogpost_list_endpoint'),
    path('tags/', tags_list, name='tags_list_endpoint'),
    path('blogpost/create/', BlogPostCreateView.as_view(),
         name='blogpost_create_endpoint'),
    path('blogpost/<str:slug>/', BlogPostDetailView.as_view(),
         name='blogpost_detail_endpoint'),
    path('blogpost/<str:slug>/update/', BlogPostUpdateView.as_view(),
         name='blogpost_update_endpoint'),
    path('tag/create/', TagCreateView.as_view(), name='tag_create_endpoint'),
    path('tag/<str:slug>/', TagDetailView.as_view(), name='tag_detail_endpoint'),
    # path('blogpost/<str:slug>/', blogpost_detail,
    #      name='blogpost_detail_endpoint'),
    # path('tag/<str:slug>/', tag_detail, name='tag_detail_endpoint'),
    path('tag/<str:slug>/update/', TagUpdateView.as_view(),
         name='tag_update_endpoint'),
]
