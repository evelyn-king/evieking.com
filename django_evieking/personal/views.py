from django.shortcuts import render
from django.conf import settings

# Create your views here.

def home(request):
    """Home page view"""
    context = {
        'site_name': settings.SITE_NAME,
        'site_description': settings.SITE_DESCRIPTION,
        'author': 'Evelyn King',
        'info': 'Physicist, Engineer, Developer',
        'since': 2024,
    }
    return render(request, 'personal/home.html', context)

def about(request):
    """About page view"""
    context = {
        'site_name': settings.SITE_NAME,
        'title': 'About Me',
        'description': 'A short introduction to Evelyn King',
        'author': 'Evelyn King',
    }
    return render(request, 'personal/about.html', context)
