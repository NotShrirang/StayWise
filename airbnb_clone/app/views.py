from .models import Country, State, Village, Views, Place, Reservation
from .serializers import CountrySerializer, StateSerializer, VillageSerializer, ViewsSerializer, PlaceSerializer, ReservationSerializer
from rest_framework import viewsets

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class VillageViewSet(viewsets.ModelViewSet):
    queryset = Village.objects.all()
    serializer_class = VillageSerializer

class ViewsViewSet(viewsets.ModelViewSet):
    queryset = Views.objects.all()
    serializer_class = ViewsSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer