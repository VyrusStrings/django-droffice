from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    dosage_instructions = models.TextField()

    def __str__(self):
        return self.name
