from django.urls import path
from . import views

urlpatterns = [
    path('parameters/', views.parameters, name='parameters'),
    path('add/', views.add_data, name='add_data'),
    path('', views.home, name='home'),

    path('export/', views.export_measurements_to_excel, name='export_data'),
]