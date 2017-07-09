from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')

def findpage(request, nav):
    return render(request, '%s.html' % nav, {'page_title': 'Home', 'nav':nav})
