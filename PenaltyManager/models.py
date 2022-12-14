from email.policy import default
from random import choices
from tkinter import CASCADE
from django.db import models
from django.conf import settings
from  django.utils import timezone

# Create your models here.
GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

OFFENCE_CHOICES = [
        ('SELECT','Select an Offence'),
        ('LSV', 'LIGHT/SIGN VIOLATION'),
        ('ROB', 'ROAD OBSTRUCTION'),
        ('RTV','ROUTE VIOLATION'),
        ('SLV', 'SPEED LIMIT VIOLATION'),
        ('VLV', 'VEHICLE LICENCE VIOLATION'),
        ('NPV','VEHICLE NUMBER PLATE VIOLATION'),
        ('DLV', "DRIVER'S LICENCE VIOLATION"),
        ('WOV', 'WRONGFUL OVERTAKING'),
        ('RMV','ROAD MARKING VIOLATION'),
        ('CSV', 'CAUTION SIGN VIOLATION'),
        ('DGD', 'DANGEROUS DRIVING'),
        ('DUI','DRIVING UNDER ALCOHOL OR DRUG INFLUENCE'),
        ('OFD', 'OPERATING A VEHICLE WITH FORGED DOCUMENTS'),
        ('UTS', 'UNAUTHORIZED REMOVAL OF OR TAMPERING WITH ROAD SIGNS'),
        ('DNM','DO NOT MOVE VIOLATION'),
        ('ICW', 'INADEQUATE CONSTRUCTION WARNING'),
        ('CAV', 'CONSTRUCTION AREA SPEED LIMIT VIOLATION'),
        ('FMO','FAILURE TO MOVE OVER'),
        ('FCM', 'FAILURE TO COVER UNSTABLE MATERIALS'),
        ('OVL', 'OVERLOADING'),
        ('TYY','DRIVING WITH WORN-OUT TYRE OR WITHOUT SPARE TYRE'),
        ('VWV', 'DRIVING WITHOUT OR WITH SHATTERED WINDSCREEN'),
        ('FFF', 'FAILURE TO FIX RED FLAG ON PROJECTED LOAD'),
        ('FRC','FAILURE TO REPORT ACCIDENT'),
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
    officer_department = models.CharField(max_length=50)
    
    def __str__(self):
        return self.officer_name

# class Offences(models.Model):
#     offence = models.CharField(max_length = 64)
#     points = models.IntegerField(blank=True, null=True)
#     category = models.IntegerField(blank=True, null=True)
#     code = models.CharField(max_length = 64)

#     def __str__(self):
#         return self.officer_name

        
class Penalty(models.Model):
    penalty_id = models.CharField(max_length = 50, unique=True)
    driver_name = models.CharField(max_length=50, blank=True, null=True)    
    # amount = models.IntegerField()
    points = models.IntegerField(blank=True, null=True)
    offence = models.CharField(max_length = 10, choices=OFFENCE_CHOICES, default='SELECT')
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



