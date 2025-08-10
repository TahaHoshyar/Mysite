from django import template
from blog.models import Post
from blog.models import Category

register = template.Library()

@register.simple_tag(name = 'totalposts')
def helo():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name = 'posts')
def helo():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=20):
    return value[:arg] + '...'

@register.inclusion_tag('blog/blog-latest-post.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by('published_date')[:3]
    return {'posts':posts}


@register.inclusion_tag('blog/blog-post-category.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categotries = Category.objects.all()
    cat_dict = {}
    for name in categotries:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}