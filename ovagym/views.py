from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {}

    return HttpResponse(template.render(context,request))

def about(request):
    template = loader.get_template('about.html')
    context = {}

    return HttpResponse(template.render(context,request))

def contact(request):
    template = loader.get_template('contact.html')
    context = {}

    return HttpResponse(template.render(context,request))

def classes(request):
    template = loader.get_template('class.html')
    context = {}

    return HttpResponse(template.render(context,request))

def single(request):
    template = loader.get_template('single.html')
    context = {}

    return HttpResponse(template.render(context,request))

def feature(request):
    template = loader.get_template('feature.html')
    context = {}

    return HttpResponse(template.render(context,request))