from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    contact_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ExaminationRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='examinations')
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='examinations/', blank=True, null=True)
    image = models.ImageField(upload_to='examinations/', blank=True, null=True)

    def __str__(self):
        return f"Examination for {self.patient}"
