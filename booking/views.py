from django.shortcuts import render

from rest_framework import viewsets
from .models import BusStation, BusRoute, Booking
from .serializers import BusStationSerializer, BusRouteSerializer, BookingSerializer

class BusStationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BusStation.objects.all()
    serializer_class = BusStationSerializer

class BusRouteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BusRoute.objects.all()
    serializer_class = BusRouteSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def map_view(request):
    return render(request, 'map.html')
