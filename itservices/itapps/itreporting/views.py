from django.shortcuts import render

from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1> Student IT Services - Home </h1>')

def about(request):
    return HttpResponse('<h1> Student IT Services - About Us </h1>')

def contact(request):
    return HttpResponse('<h1> Student IT Services - Contact Us </h1>')