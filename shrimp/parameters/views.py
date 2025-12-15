 

# Create your views here.

 
from django.http import HttpResponse
from django.utils import timezone
from django.utils.timezone import make_naive
from django.template import loader
from django.shortcuts import render
from .models import Measurement
from .models import Tank
import pandas as pd 

def home(request):
    return render(request, "home.html")

#shows all parameter measurements. add chartJS later. 


def parameters(request):
    data_ammonia=[]
    data_nitrate=[]
    data_nitrite=[]


    labels=[]

    measurements=Measurement.objects.order_by('-date')

    for m in measurements:
     labels.append(m.date.strftime("%Y-%m-%d %H:%M:%S"))
     data_ammonia.append(m.ammonia)
     data_nitrate.append(m.nitrates)
     data_nitrite.append(m.nitrites)


    return render(request, "allparams.html", {
        "labels": labels,
        "data_ammonia": data_ammonia,
        "data_nitrate": data_nitrate,
        "data_nitrite": data_nitrite,
        })





# add measurements to tank

from .forms import MeasurementForm

def add_data(request):
    context = {}
    form = MeasurementForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "add.html", context)

#export to excel


def export_measurements_to_excel():
 
    measurements = Measurement.objects.all()

    data = []
    for m in measurements:
        data.append({
            "Tank Brand": m.tank.brand,
            "Tank Size (liters)": m.tank.size_liters,
            "Water Type": m.tank.water_type,
            "Date": make_naive(m.date), #get past timezone error
            "Ammonia": m.ammonia,
            "Nitrites": m.nitrites,
            "Nitrates": m.nitrates,
        })

    df = pd.DataFrame(data)

    # Define the Excel file response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=measurements.xlsx'

    # Use Pandas to write the DataFrame to an Excel file
    df.to_excel(response, index=False, engine='openpyxl')

    return response 

