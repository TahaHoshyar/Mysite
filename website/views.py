from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def about_views(request):
    return render(request,'website1/about.html')

def index_views(request):
    return render(request,'website1/index.html')

def contact_views(request):
    return render(request,'website1/contact.html')
def elements_views(request):
    return render(request,'website1/elements.html')