from django.shortcuts import render
from django.template import loader


# Create your views here.

from django.http import HttpResponse

def parameters(request):
  template = loader.get_template('params.html')
  return HttpResponse(template.render())