from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm


def index(request):
    blog = Blog.objects.order_by('-id')
    cont = {'blog': blog}
    return render(request, 'blog/index.html', cont)


def about(request):
    return render(request, 'blog/about.html')


def change(request, post_slug):
    post = get_object_or_404(Blog, slug=post_slug)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = BlogForm(instance=post)
    contex = {'form': form}
    return render(request, 'blog/change.html', contex)


def helper(request):
    return render(request, 'blog/help.html')


def wort(request, post_slug):
    blog = Blog.objects.filter(slug=post_slug)
    con = {'blog': blog}
    return render(request, 'blog/wort.html', con)
