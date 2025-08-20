from django.shortcuts import render , get_object_or_404 , redirect
from blog.models import Post , Comment
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from blog.forms import CommentForm
from django.contrib import messages

# Create your views here.

def blog_views(request,**kwargs):
    post = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        post = post.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        post = post.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        post = post.filter(tags__name__in=[kwargs['tag_name']])
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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your comment submitted successfully')
        else:
            messages.add_message(request,messages.ERROR,'your comment did not submit')
            
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)
    if not post.login_require:
        comments = Comment.objects.filter(post=post.id,approved=True)
        form = CommentForm()
        context = {'post':post , 'comments':comments , 'form':form}
        return render(request , 'blog/blog-single.html',context)
    else:
        return redirect('/accounts/login')

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
