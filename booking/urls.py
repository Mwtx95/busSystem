from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusStationViewSet, BusRouteViewSet, BookingViewSet
from booking.views import map_view
from django.contrib import admin

router = DefaultRouter()
router.register(r'bus-stations', BusStationViewSet, basename='busstation')
router.register(r'bus-routes', BusRouteViewSet, basename='busroute')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', map_view, name='map'),
]