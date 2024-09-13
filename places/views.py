from rest_framework import viewsets, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend

from places.models import Place
from places.serializers import PlaceSerializer
from places.filters import PlaceFilter


class PlaceView(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filterset_class = PlaceFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = [
        'name',
        'description',
        'address',
        'city__name',
        'city__state__name',
        'city__state__country__name',
    ]
    ordering_fields = [
        'name',
        'price',
        'rating',
        'guest_capacity',
        'bedrooms',
        'beds',
        'bathrooms',
        'createdAt',
        'updatedAt',
    ]
    ordering = ['-createdAt']
