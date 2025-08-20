
from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed

app_name = 'blog'

urlpatterns = [
    path('',blog_views,name = 'index'),
    path('<int:pid>',blog_single,name = 'single'),
    path('category/<str:cat_name>',blog_views,name = 'category'),
    path('author/<str:author_username>' , blog_views , name= 'author' ), 
    path('tag/<str:tag_name>' , blog_views , name= 'tag' ), 
    path('search/',blog_search , name='search'),
    path('test' , test_views , name= 'test'),
    path('rss/feed/' , LatestEntriesFeed()),

]
 #    path('category/<str:cat_name>',blog_category,name = 'category'),