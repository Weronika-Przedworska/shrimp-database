from django.urls import path
from . import views

urlpatterns = [
    path('parameters/', views.parameters, name='parameters'),
    #path('/', views.parameters, name='parameters'),

    path('export/', views.export_measurements_to_excel, name='export-measurements'),
]