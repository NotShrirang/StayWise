from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReservationView

router = DefaultRouter()
router.register(r'reservations', ReservationView)

urlpatterns = [
    path('', include(router.urls)),
]
