from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
class Patient(models.Model):
    id=models.UUIDField(default=uuid4,primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    condition = models.TextField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    id=models.UUIDField(default=uuid4,primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctors')
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='mappings')

    class Meta:
        unique_together = ('patient', 'doctor')

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"
