from django import forms
from .models import Measurement

class MeasurementForm (forms.ModelForm):
    class Meta:
        model = Measurement
        exclude = ['date']   # date is collected automatically so no need to enter
