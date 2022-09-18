from django.db import models
from user.models import User

# Create your models here.
class Garage(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bike_slots = models.IntegerField(default=0)
    car_slots = models.IntegerField(default=0)
    f_bike_slots = models.IntegerField(default=0)
    f_car_slots = models.IntegerField(default=0)
    bike_rate = models.DecimalField(max_digits=5, decimal_places=2)
    car_rate = models.DecimalField(max_digits=5, decimal_places=2)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ParkingRecord(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    garage_id = models.ForeignKey(Garage, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    phnno = models.BigIntegerField(null=False)
    carno = models.CharField(max_length=15, null=False)
    regtime = models.DateTimeField(auto_now_add=True)
    exittime = models.DateTimeField(auto_now_add=True)
    slotno = models.CharField(max_length=10)
    amt = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    ispaid = models.BooleanField(default=False)
    isCar = models.BooleanField(default=True)

    def __str__(self):
        return self.carno + " - " + str(self.phnno)


class OTP(models.Model):
    carno = models.CharField(max_length=15, null=False)
    garage_id = models.BigIntegerField(null=False)
    phnno = models.BigIntegerField(null=False)
    otp = models.IntegerField()
