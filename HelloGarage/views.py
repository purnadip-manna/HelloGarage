from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    data={
        "slot_available" : 10,
        "cars" : 20
    }
    return render(request, "index.html", context=data)


# 