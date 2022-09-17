import datetime
from django.db import models

# Create your models here.
class ParkingRecord(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255)
    phnno = models.BigIntegerField(null=False)
    carno = models.CharField(max_length=15, null=False)
    regtime = models.DateTimeField()
    exittime = models.DateTimeField()
    slotno = models.CharField(max_length=10)
    

class Garage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slotno = models.IntegerField(null=False)
    
