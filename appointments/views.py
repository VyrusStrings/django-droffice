from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AppointmentForm, BusyHourForm
from .models import Appointment, BusyHour
from .utils import sync_to_google_calendar

@login_required
def create_appointment(request):
    if not request.user.is_secretary:
        messages.error(request, "Permission denied.")
        return redirect('home')
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            try:
                appointment.clean()
                appointment.save()
                sync_to_google_calendar(appointment)  # Stubbed sync
                messages.success(request, "Appointment created successfully.")
                return redirect('appointments:list')
            except Exception as e:
                messages.error(request, str(e))
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AppointmentForm()
    return render(request, 'appointments/create_appointment.html', {'form': form})

@login_required
def list_appointments(request):
    if not (request.user.is_secretary or request.user.is_doctor):
        messages.error(request, "No permission.")
        return redirect('home')
    appointments = Appointment.objects.all().order_by('date', 'start_time')
    return render(request, 'appointments/list_appointments.html', {'appointments': appointments})

@login_required
def create_busy_hour(request):
    if not request.user.is_doctor:
        messages.error(request, "Permission denied.")
        return redirect('home')
    if request.method == 'POST':
        form = BusyHourForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Busy hour added.")
            return redirect('appointments:busy_hours_list')
        else:
            messages.error(request, "Please correct the errors.")
    else:
        form = BusyHourForm()
    return render(request, 'appointments/create_busy_hour.html', {'form': form})

@login_required
def list_busy_hours(request):
    if not request.user.is_doctor:
        messages.error(request, "Permission denied.")
        return redirect('home')
    busy_hours = BusyHour.objects.all().order_by('date', 'start_time')
    return render(request, 'appointments/list_busy_hours.html', {'busy_hours': busy_hours})
