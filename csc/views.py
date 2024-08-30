from csc.models import (
    City,
    State,
    Country
)
from csc.serializers import (
    CitySerializer,
    StateSerializer,
    CountrySerializer
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, filters
from django_filters.rest_framework import DjangoFilterBackend


class CityView(ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ('name', 'state__name', 'state__country__name')
    search_fields = ('name', 'state__name', 'state__country__name')

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(
            self.queryset.filter(isActive=True).order_by('name'))
        serializer = CitySerializer(qs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return Response({"error": "You are not authorized to create a city"}, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        return Response({"error": "You are not authorized to create a city"}, status=status.HTTP_401_UNAUTHORIZED)

    def partial_update(self, request, *args, **kwargs):
        return Response({"error": "You are not authorized to create a city"}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        return Response({"error": "You are not authorized to create a city"}, status=status.HTTP_401_UNAUTHORIZED)


class StateView(ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CountryView(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)