from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaceReservationView

router = DefaultRouter()
router.register(r'place-reservations', PlaceReservationView)

urlpatterns = [
    path('', include(router.urls)),
]
