from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import models
from website.models import Project, ProjectType

def index(request):
    return render(request, 'index.html')

def findpage(request, nav):
    if nav == 'projects':
        project_dict = {} 
        project_types = ProjectType.objects.all()
        for x in project_types:
            projects = Project.objects.filter(project_type=x)
            if len(projects) != 0:
                project_dict[x.title] = projects
        return render(request, 'projects.html', { 'project_types': project_dict, 'nav':nav, 'page_title': 'Home' }) 
    return render(request, '%s.html' % nav, {'page_title': 'Home', 'nav':nav})
