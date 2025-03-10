from django.db import models

from django.contrib.gis.db import models

class BusStation(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()  # Stores spatial point data

    def __str__(self):
        return self.name


class BusRoute(models.Model):
    name = models.CharField(max_length=100)
    route = models.LineStringField()  # Stores spatial line data

    def __str__(self):
        return self.name


class Booking(models.Model):
    passenger_name = models.CharField(max_length=100)
    station = models.ForeignKey(BusStation, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger_name} - Seat {self.seat_number}"
