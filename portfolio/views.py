from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def aboutme(request):
    return render(request, 'portfolio/aboutme.html')
