from django.contrib import admin
from .models import Measurement
from .models import Tank

# register measurement, tank models

admin.site.register(Measurement)
admin.site.register(Tank)