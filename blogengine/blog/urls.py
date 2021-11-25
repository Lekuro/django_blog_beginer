from django.urls import path
from blog.views import hello, blogposts_list

urlpatterns = [
    path('hello/', hello),
    path('blogposts/', blogposts_list)
]
