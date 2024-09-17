from rest_framework import viewsets
from .models import Reservation
from .serializers import ReservationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['place', 'user', 'start_datetime', 'end_datetime']
    search_fields = ['place', 'user']
    ordering_fields = ['start_datetime', 'end_datetime', 'registered_at']
    ordering = ['start_datetime']
