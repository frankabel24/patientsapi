from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length= 80)
    address = models.CharField(max_length=255)
    ZipCode = models.IntegerField()
    phone = models.PositiveIntegerField()
    gender = models.CharField(max_length=9)
    email = models.EmailField

