import json
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from gapp.queires import get_garage_details, get_vehicle, get_active_vehicle, create_new_record, otp_gen, update_number, val_otp, charge_calculate

from .msg_send import *


# Create your views here.
def admin(request):
    if request.user.is_anonymous:
        messages.add_message(request, messages.INFO, 'Have to Login first')
        return redirect("login_view")

    else:
        user = request.user
        g = get_garage_details(user)
        vehicles = get_active_vehicle(g.id)
        data = {
            "name" : g.name,
            "address" : g.address,
            "car" : g.f_car_slots,
            "bike" : g.f_bike_slots,
            "car_slot" : g.car_slots,
            "bike_slot" : g.bike_slots,
            "bike_rate" : g.bike_rate,
            "car_rate" : g.car_rate,
            "vehicles" : vehicles
        }
        return render(request, "adminpanel.html", context=data)

@csrf_exempt
def newvehicle(request):
    if (request.method == "POST"):
        received_json_data=json.loads(request.body)
        garage_id = received_json_data["garage_id"]
        carno = received_json_data["carno"]
        try:
            create_new_record(garage_id, carno)
            return HttpResponse("Done")
        except:
            return HttpResponse("Failed")
    else:
        return HttpResponse("Failed")


def update_parking_details(request, carno, garageid):
    record = get_vehicle(garageid, carno)
    if(record.phnno == 0):
        data = {
            "gid" : garageid,
            "carno" : record.carno,
            "regtime" : record.regtime,
            "isCar" : record.isCar
        }
        return render(request, "filldetails.html", context=data)
    else:
        return HttpResponse("<big>Already Registered!</big>")

@csrf_exempt
def vregister(request):
    if (request.method == "POST"):
        gid = request.POST.get("gid")
        vno = request.POST.get("vno")
        phnno = request.POST.get("phnno")
        n = otp_gen(gid, vno, phnno)
        sendmsg(n, phnno, "Parking")
        print("OTP:", n)
        data = {
            "phnno":phnno,
            "carno":vno,
            "exit" : "false"
        }
        return render(request, "otp.html", context=data)


@csrf_exempt
def votp(request):
    if (request.method == "GET"):
        otp = request.GET.get("otp")
        phnno = request.GET.get("phnno")
        carno = request.GET.get("carno")
        flag = request.GET.get("flag")
        if(flag == "false"):
            try:
                val_otp(otp, phnno, carno)
                update_number(carno, phnno)
                return HttpResponse("<big>Successfully Registered! Opening Gate!</big>")
            except:
                return HttpResponse("<big>Failed to Verify!</big>")
        else:
            try:
                val_otp(otp, phnno, carno)
                # Calculate charge Rate
                amt = charge_calculate(phnno, carno)
                return HttpResponse(f"<big>You have to pay : <b>Rs.{amt}</b></big>")
            except:
                return HttpResponse("<big>Failed to Verify!</big>")

def exit_verify(request, carno, garageid):
    record = get_vehicle(garageid, carno)
    phnno = record.phnno
    n = otp_gen(garageid, carno, phnno)
    sendmsg(n, phnno, "Payment")
    print("OTP:", n)
    data = {
        "phnno":phnno,
        "carno":carno,
        "exit" : "true"
    }
    return render(request, "otp.html", context=data)