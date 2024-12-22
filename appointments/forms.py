from django import forms
from .models import Appointment, BusyHour

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'date', 'start_time', 'end_time']

class BusyHourForm(forms.ModelForm):
    class Meta:
        model = BusyHour
        fields = ['date', 'start_time', 'end_time']
