from rest_framework import viewsets, filters, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from places.models import Place, PlaceImage
from places.serializers import PlaceSerializer, PlaceImageSerializer
from places.filters import PlaceFilter, PlaceImageFilter


class PlaceView(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filterset_class = PlaceFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
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

    def create(self, request, *args, **kwargs):
        current_user = request.user
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
        return super().create(request, *args, **kwargs)


class PlaceImageView(viewsets.ModelViewSet):
    queryset = PlaceImage.objects.all()
    serializer_class = PlaceImageSerializer
    filterset_class = PlaceImageFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    ordering_fields = [
        'createdAt',
        'updatedAt',
    ]
    ordering = ['-createdAt']
