import datetime
from unicodedata import name
from django.db import models

# Create your models here.
class ParkingRecord(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255)
    phnno = models.BigIntegerField(max_length=10, null=False)
    carno = models.CharField(max_length=15, null=False)
    regtime = models.DateTimeField(default=datetime.datetime.now())
    exittime = models.DateTimeField()
    slotno = models.CharField()
    

class Garage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    slotno = models.IntegerField(null=False)
    
