from django.http import HttpResponse
from django.utils import timezone
from django.utils.timezone import make_naive
from django.template import loader
from django.shortcuts import render
from .models import Measurement
from .models import Tank
import pandas as pd 


# home page view 
def home(request):
    return render(request, "home.html")

# random shrimp page view 
def random(request):
    return render(request, "random.html")

# data input view 
def parameters(request):
    data_ammonia=[]
    data_nitrate=[]
    data_nitrite=[]


    labels=[]

    measurements=Measurement.objects.order_by('-date')

    for m in measurements:
     labels.append(m.date.strftime("%Y-%m-%d %H:%M:%S")) # need to do this to get string version of the timestamp 
     data_ammonia.append(m.ammonia)
     data_nitrate.append(m.nitrates)
     data_nitrite.append(m.nitrites)


    return render(request, "allparams.html", {
        "labels": labels,
        "data_ammonia": data_ammonia,
        "data_nitrate": data_nitrate,
        "data_nitrite": data_nitrite,
        })

# view to add measurements to tank

from .forms import MeasurementForm

def add_data(request):

    context = {}
    form = MeasurementForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "add.html", context)

#view to export data to Excel file
def export_measurements_to_excel(request):
 
    measurements = Measurement.objects.all()

    data = []

    for m in measurements:
        data.append({
            "Tank Brand": m.tank.brand, # parent tank attribute
            "Tank Size (liters)": m.tank.size_liters, # parent tank attribute
            "Water Type": m.tank.water_type, # parent tank attribute
            "Date": make_naive(m.date), # need to do this to get past timezone error
            "Ammonia": m.ammonia,  
            "Nitrites": m.nitrites,
            "Nitrates": m.nitrates,
        })

    df = pd.DataFrame(data)

    # Define the Excel file response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=measurements.xlsx'
    df.to_excel(response, index=False, engine='openpyxl')
    return response 

