from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about_views(request):
    return render(request,'about.html')

def index_views(request):
    return render(request,'index.html')

def contact_views(request):
    return render(request,'contact.html')
def web_views(request):
    return render(request,'website1/web.html')