from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PatientForm, ExaminationRecordForm
from .models import Patient

@login_required
def create_patient(request):
    if not request.user.is_secretary:
        messages.error(request, "You do not have permission.")
        return redirect('home')
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Patient created successfully.")
            return redirect('patients:list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PatientForm()
    return render(request, 'patients/create_patient.html', {'form': form})

@login_required
def list_patients(request):
    if not (request.user.is_secretary or request.user.is_doctor):
        messages.error(request, "No permission.")
        return redirect('home')
    patients = Patient.objects.all()
    return render(request, 'patients/list_patients.html', {'patients': patients})

@login_required
def create_examination_record(request):
    if not request.user.is_doctor:
        messages.error(request, "You do not have permission.")
        return redirect('home')

    if request.method == 'POST':
        form = ExaminationRecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Examination record created.")
            return redirect('patients:list') 
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ExaminationRecordForm()

    return render(request, 'patients/create_examination.html', {'form': form})
