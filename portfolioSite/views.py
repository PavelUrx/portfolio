from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from portfolioSite.models import *

def index(request):
    template = loader.get_template('index.html')
    textContent = {'textContent' : Index.objects.all()}
    projectsContent = {'projectsContent' : Projects.objects.all()}
    context = textContent | projectsContent
    return HttpResponse(template.render(context))
