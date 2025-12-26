from django.shortcuts import redirect, render, get_object_or_404
from .models import Blogs, Category, Comment
from django.db.models import Q
from django.http import HttpResponseRedirect


def posts_by_category(request, category_id):
    posts = Blogs.objects.filter(status='Published', category=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blogs, slug=slug, status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = Comment.objects.filter(blog=single_blog).count()
    context = {
        'single_blog': single_blog,
        'comments' : comments,
        'comment_count' : comment_count
    }
    return render(request, 'blogs.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(
        short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context = {
        'searched_blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search.html', context)
