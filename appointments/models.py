from django.db import models
from patients.models import Patient
from django.core.exceptions import ValidationError

class BusyHour(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Busy: {self.date} {self.start_time}-{self.end_time}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def clean(self):
        # Check busy hours conflict
        busy_periods = BusyHour.objects.filter(date=self.date)
        for b in busy_periods:
            if self.start_time < b.end_time and self.end_time > b.start_time:
                raise ValidationError("Appointment conflicts with busy hours.")

        # Check appointment conflicts
        existing_appointments = Appointment.objects.filter(date=self.date).exclude(pk=self.pk)
        for a in existing_appointments:
            if self.start_time < a.end_time and self.end_time > a.start_time:
                raise ValidationError("Appointment conflicts with another appointment.")

    def __str__(self):
        return f"Appointment for {self.patient} on {self.date} at {self.start_time}-{self.end_time}"
