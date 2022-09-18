import math
import datetime
from random import randint
from .models import Garage, ParkingRecord, OTP

def get_garage_by_id(id):
    try:
        garage = Garage.objects.get(id = id)
        return garage
    except:
        return None

def get_garage_details(user_id):
    try:
        garage = Garage.objects.get(user_id = user_id)
        return garage
    except:
        return None

def get_active_vehicle(garage_id):
    try:
        vehicle = ParkingRecord.objects.filter(garage_id=garage_id, ispaid=False)
        return vehicle
    except:
        return None

def get_vehicle(garage_id, carno):
    try:
        vehicle = ParkingRecord.objects.get(garage_id=garage_id, carno=carno, ispaid=False)
        return vehicle
    except:
        return None

def create_new_record(garage_id, carno):
    garage = get_garage_by_id(garage_id)
    pr = ParkingRecord(garage_id=garage, name="x", phnno = 0, carno=carno, slotno="S1")
    garage.f_car_slots = garage.f_car_slots + 1
    garage.save()
    pr.save()

def update_number(carno, phnno):
    pr = ParkingRecord.objects.get(carno=carno, ispaid=False)
    pr.phnno = int(phnno)
    pr.save()

def otp_gen(garage_id, carno, phnno):
    n = randint(1000, 9999)
    otp = OTP(carno=carno, garage_id=garage_id, phnno=phnno, otp=n)
    otp.save()
    return n

def val_otp(otp, phnno, carno):
    c = OTP.objects.get(carno=carno, phnno=int(phnno), otp=otp)
    c.delete()
    return True

def charge_calculate(phnno, carno):
    record = ParkingRecord.objects.get(phnno=phnno, carno=carno, ispaid=False)
    starttime = record.regtime
    record.exittime = datetime.datetime.now()
    endtime = record.exittime
    diff = endtime-starttime.replace(tzinfo=None)
    hrs = math.ceil((diff.total_seconds() / 60)/ 60)
    if record.isCar:
        rate = record.garage_id.car_rate
        record.garage_id.f_car_slots = record.garage_id.f_car_slots-1
        record.garage_id.save()
    else:
        rate = record.garage_id.bike_rate
        record.garage_id.f_bike_slots = record.garage_id.f_bike_slots-1
        record.garage_id.save()

    amt = hrs*rate
    record.amt = amt
    record.ispaid = True  # Need to change later (ispaid - True when payment is done)
    record.save()
    return amt