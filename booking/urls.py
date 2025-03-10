from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BusStationViewSet, BusRouteViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'bus-stations', BusStationViewSet, basename='busstation')
router.register(r'bus-routes', BusRouteViewSet, basename='busroute')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('api/', include(router.urls)),
]