from rest_framework import viewsets
from .models import PlaceReservation
from .serializers import PlaceReservationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class PlaceReservationView(viewsets.ModelViewSet):
    queryset = PlaceReservation.objects.all()
    serializer_class = PlaceReservationSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['place', 'user', 'start_datetime', 'end_datetime']
    search_fields = ['place', 'user']
    ordering_fields = ['start_datetime', 'end_datetime', 'registered_at']
    ordering = ['start_datetime']
