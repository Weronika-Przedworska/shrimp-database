 

# Create your views here.

 
from django.http import HttpResponse
from django.utils import timezone
from django.utils.timezone import make_naive
from django.template import loader
from django.shortcuts import render
from .models import Measurement
from .models import Tank
import pandas as pd 
 
#shows all parameter measurements. add chartJS later. 
def parameters(request):
    myparams = Measurement.objects.all()
    # mytank=Tank.objects.all()
    return render(request, "allparams.html", {
        "myparams": myparams
    })

# add measurements to tank


#export to excel


def export_measurements_to_excel(request):
 
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
        })

    df = pd.DataFrame(data)

    # Define the Excel file response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=measurements.xlsx'

    # Use Pandas to write the DataFrame to an Eaxcel file
    df.to_excel(response, index=False, engine='openpyxl')

    return response 