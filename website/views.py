from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import models
from website.models import Project

def index(request):
    return render(request, 'index.html')

def findpage(request, nav):
    if nav == 'projects':
        project_list = Project.objects.all()
        return render(request, 'projects.html', { 'projects': project_list, 'nav':nav, 'page_title': 'Home' }) 
    return render(request, '%s.html' % nav, {'page_title': 'Home', 'nav':nav})
