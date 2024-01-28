from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    about_link = '<a href="/rango/about/">About</a>'
    return HttpResponse(f"Rango says hey there partner! Visit the {about_link}.")

def about(request):
    index_link = '<a href="/rango/">Index</a>'
    return HttpResponse(f"Rango says here is the about page. Visit the {index_link}.")
