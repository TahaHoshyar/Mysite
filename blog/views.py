from django.shortcuts import render , get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
# Create your views here.

def blog_views(request, cat_name=None, author_username=None):
    post = Post.objects.filter(status=1)
    if cat_name:
        post = post.filter(category__name=cat_name)
    if author_username:
        post = post.filter(author__username=author_username)
    post = Paginator(post, 3)
    try:
        page_number = request.GET.get('page')
        post = post.get_page(page_number)
    except PageNotAnInteger:
        post = post.get_page(1)
    except EmptyPage:
        post = post.get_page(1)
    context = {'post':post}
    return render(request, 'blog/blog-home.html', context)
    
def blog_single(request,pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    #post = Post.objects.all()
    #post = Post.objects.filter(status=1)
    context = {'post':post}
    return render(request , 'blog/blog-single.html',context)

def test_views(request):
    return render(request , 'test.html') 

def blog_category(request, cat_name):
    post = Post.objects.filter(status=1)
    post = post.filter(category__name=cat_name)
    
    context = {'post':post}
    return render(request, 'blog/blog-home.html', context)

# def blog_search(request):
#     post = Post.objects.filter(status=1)
#     if request.method == 'GET':
#         post = post.filter(content__contains=request.GET.get('s'))          #this is good but there is another code to this function and i write it in the under this code
#     context = {'post':post}
#     return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    post = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            post = post.filter(content__contains=s)
    context = {'post':post}
    return render(request, 'blog/blog-home.html', context)
