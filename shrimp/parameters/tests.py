
import pytest
from .models import Measurement
from .models import Tank
from django.urls import reverse




@pytest.mark.django_db

def test_tank_measurement():
    tank = Tank.objects.create(
        size_liters= 10,
        brand="Fluval",
        water_type="freshwater",
    )
    measurement = Measurement.objects.create(
        tank=tank,
        ammonia = 5,
        nitrates=6,
        nitrites=7,
    )
    
    # check tank
    assert tank.brand == "Fluval"
    assert tank.size_liters == 10
    assert tank.water_type == "freshwater"
    assert tank.id != None


    #check measurements
    assert measurement.ammonia == 5
    assert measurement.nitrates == 6
    assert measurement.nitrites == 7
    assert measurement.id != None


    #check that measurements belong to the right tank
    assert measurement.tank == tank

    #check that one instance of each model was made
    assert Measurement.objects.count() == 1 
    assert Tank.objects.count() == 1 


# check that views can load

@pytest.mark.django_db

def test_adding(client):
    url = reverse('add_data')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db

def test_showing(client):
    url = reverse('parameters')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db

def test_home(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db

def test_excel(client):
    url = reverse('export_data')
    response = client.get(url)
    assert response.status_code == 200

    


