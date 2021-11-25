from django.urls import path
from blog.views import *

urlpatterns = [
    path('hello/', hello),
    path('blogposts/', blogposts_list, name='blogpost_list_endpoint'),
    path('blogpost/<str:slug>/', blogpost_detail,
         name='blogpost_detail_endpoint'),
]
