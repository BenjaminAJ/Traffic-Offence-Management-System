from django.db import models
from django.conf import settings
from  django.utils import timezone

# Create your models here.

class Driver(models.Model):
    driver_firstname = models.CharField(max_length=50)
    driver_lastname = models.CharField(max_length=50)
    driver_license = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    vehicle_plate = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.driver_firstname

class Officer(models.Model):
    officer_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.officer_name
        
class Penalty(models.Model):
    penalty_id = models.CharField(max_length = 128)
    amount = models.IntegerField()
    points = models.IntegerField()
    type = models.CharField(max_length = 64)
    category = models.IntegerField()
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f"RFID: {self.penalty_id}\nStatus: {self.status}\nAmount: {self.amount}\nType: {self.type}\nDate: {self.date}"


# class Comment(models.Model):
 #   post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
  #  author = models.CharField(max_length=200)
   # text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
   # approved_comment = models.BooleanField(default=False)
#
 #   def approve(self):
  #      self.approved_comment = True
   #     self.save
    #
   # def __str__(self):
    #    return self.text

