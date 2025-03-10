from django.contrib import admin

from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import BusStation, BusRoute, Booking

@admin.register(BusStation)
class BusStationAdmin(GISModelAdmin):
    list_display = ("name", "location")

@admin.register(BusRoute)
class BusRouteAdmin(GISModelAdmin):
    list_display = ("name", "route")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("passenger_name", "station", "seat_number", "timestamp")