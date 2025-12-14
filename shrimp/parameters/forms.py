from django import forms
from .models import Measurement

class MeasurementForm (forms.ModelForm):
    class Meta:
        model = Measurement
       # fields = "__all__"  # or list fields explicitly for security
        exclude = ['date']
