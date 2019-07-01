from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm
from django.views.decorators.http import require_POST
from django.views.generic import ListView

def home(request):
    blogs = Blog.objects.order_by('-created_datetime', 'origin')
    # blogs = get_object_or_404(Blog)
    return render(request, 'blogs/home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    # blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})

def blog_list(request):
    blogs = Blog.objects.order_by('-created_datetime', 'origin')
    return render(request, 'blogs/blog_list.html', {'blogs':blogs})

def new_form(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            context_object_name = 'image_list'
            model.save()
            return redirect('blogs:new_form')
    else:
        form = BlogForm()
    return render(request, 'blogs/new_form.html', {'form': form})

def form_detail(request, blog_id):
    if request.method == "POST":
        blog = Blog.objects.get(id=blog_id)
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            model = form.save(commit=False)
            model.user = request.user
            context_object_name = 'image_list'
            model.save()
            return redirect('blogs:blog_list')
    else:
        blog = Blog.objects.get(id=blog_id)
        form = BlogForm(instance=blog)
    return render(request, 'blogs/form_detail.html', {'form': form, 'blog': blog})

@require_POST #POSTメソッドの時だけ、削除する
def form_delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blogs:blog_list')
    return render(request, 'blogs/form_delete.html', {'blog': blog})
