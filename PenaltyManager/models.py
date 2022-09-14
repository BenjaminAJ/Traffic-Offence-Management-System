from tkinter import CASCADE
from django.db import models
from django.conf import settings
from  django.utils import timezone

# Create your models here.
GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

# class Driver(models.Model):
#     driver_name = models.CharField(max_length=50)
#     driver_license = models.CharField(max_length=50, blank=True)
#     gender = models.CharField(max_length=1,choices=GENDER_CHOICES,
#         default='M',)
#     vehicle_plate = models.CharField(max_length=20, blank=True)
    
#     def __str__(self):
#         return self.driver_name

class Officer(models.Model):
    officer_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.officer_name
        
class Penalty(models.Model):
    penalty_id = models.CharField(max_length = 50, unique=True)
    driver_name = models.CharField(max_length=50, blank=True, null=True)    
    # amount = models.IntegerField()
    points = models.IntegerField(blank=True, null=True)
    offence = models.CharField(max_length = 64)
    category = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(default = timezone.now)
    address = models.TextField(blank=True)
    officer_name = models.ForeignKey(Officer, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,
        default='M',)
    # vehicle_plate = models.ForeignKey(Driver, related_name='reported_vehicle', on_delete=models.CASCADE, null=True)
    vehicle_plate = models.CharField(max_length=20, blank=True, null=True)
    driver_license = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.penalty_id
