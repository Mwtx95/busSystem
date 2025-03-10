from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import BusStation, BusRoute, Booking

class BusStationSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BusStation
        fields = ('id', 'name')
        geo_field = 'location'  # This is the spatial field

class BusRouteSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = BusRoute
        fields = ('id', 'name')
        geo_field = 'route'  # This is the spatial field

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
