 

# Create your views here.

 
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Measurement
from .models import Tank

def parameters(request):
    myparams = Measurement.objects.all()
    return render(request, "allparams.html", {
        "myparams": myparams
    })



#add one more view for adding values