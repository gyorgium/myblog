from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView
)

from .models import Post

class PostListView(ListView):
    template_name = 'blog/post_list.html'
    queryset = Post.objects.filter(
        status=1
    ).order_by('-created_on')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class AllPostListView(ListView):
    template_name='blog/all_post_list.html'
    queryset = Post.objects.all().order_by('-created_on')