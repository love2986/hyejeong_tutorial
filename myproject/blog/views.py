from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {
        'post_list':post_list,
    })


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })


def comment_new(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail', pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_form.html', {
        'form':form,
    })
