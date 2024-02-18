from .models import Post
from django.http import Http404
from django.shortcuts import render, get_object_or_404 

### Trae la lista entera ###

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

### Post vista individual ###

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html', {'post': post})
