from django.shortcuts import render, redirect
from django.contrib import messages

from gapp.queires import get_garage_details

def index(request):
    return render(request, "index.html")


def home(request):
    if request.user.is_anonymous:
        messages.add_message(request, messages.INFO, 'Have to Login first')
        return redirect("login_view")

    else:
        user = request.user
        g = get_garage_details(user)
        data = {
            "name" : g.name,
            "address" : g.address,
            "car" : g.f_car_slots,
            "bike" : g.f_bike_slots,
            "car_slot" : g.car_slots,
            "bike_slot" : g.bike_slots,
            "bike_rate" : g.bike_rate,
            "car_rate" : g.car_rate
        }
        return render(request, "dashboard.html", context=data)