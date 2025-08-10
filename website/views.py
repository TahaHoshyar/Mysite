from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm , ContactForm , NewsletterForm
from django.contrib import messages
# Create your views here.

def about_views(request):
    return render(request,'website1/about.html')

def index_views(request):
    return render(request,'website1/index.html')

def contact_views(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket submited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your ticket did not submited successfully')
    form = ContactForm()
    return render(request,'website1/contact.html',{'form':form})


def newsletter_views(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')



def test_views(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('form is valid')
            
        else:
            return HttpResponse('form is not valid')

    
    form = ContactForm()
    return render(request , 'test.html',{'form':form})