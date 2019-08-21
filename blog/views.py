from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView, DetailView, TemplateView,
    CreateView, UpdateView, DeleteView
)

from .models import Post, Comment
from .forms import PostForm, CommentForm

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    template_name = 'post_list.html'

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'post_detail.html'
    form_class = PostForm
    model = Post

class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'post_detail.html'
    form_class = PostForm
    model = Post

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')

class DraftListView(LoginRequiredMixin, ListView):
    template_name='post_draft_list.html'

    def get_queryset(self):
        return Post.objects.filter(status=0).order_by('-created_on')

###############################################
## Functions that require a slug or pk match ##
###############################################

@login_required
def publish_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.publish()
    return redirect('post_detail', slug=slug)

@login_required
def add_comment_to_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'comment_form.html', {'form': form})


@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', slug=comment.post.slug)


@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_slug = comment.post.slug
    comment.delete()
    return redirect('post_detail', slug=post_slug)