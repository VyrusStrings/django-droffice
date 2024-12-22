from django import forms
from .models import Patient, ExaminationRecord

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'contact_info']

class ExaminationRecordForm(forms.ModelForm):
    class Meta:
        model = ExaminationRecord
        fields = ['patient', 'notes', 'document', 'image']
