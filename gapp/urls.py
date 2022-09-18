from django.urls import path
from .views import *

urlpatterns = [
    path("", admin),
    path("newvehicle", newvehicle),
    path("update/<str:carno>/<int:garageid>", update_parking_details),
    path("exitverify/<str:carno>/<int:garageid>", exit_verify),
    path("vregister/", vregister, name="vregister"),
    path("votp/", votp, name="votp")
]
