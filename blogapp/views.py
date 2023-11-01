from django.shortcuts import render, redirect, get_object_or_404

from blogapp.forms import PostForm
from blogapp.models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'blogapp/index.html', {"posts": posts})


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blogapp/create.html', {"form": form})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blogapp/detail.html', {"post": post})


def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post.title = title
        post.content = content
        post.save()
        return redirect('detail',pk=post.pk)

    return render(request, 'blogapp/edit.html',{'post':post})


def delete(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')
