from django.shortcuts import redirect, render, get_object_or_404
from .models import Blogs, Category


# Create your views here.

def posts_by_category(request, category_id):
    posts = Blogs.objects.filter(status='Published', category=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts' : posts,
        'category' : category
    }
    return render(request, 'posts_by_category.html', context)   

def blogs(request, slug):
    single_blog = get_object_or_404(Blogs, slug=slug, status='Published')
    context = {
        'single_blog' : single_blog
    }
    return render(request, 'blogs.html', context)