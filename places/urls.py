from places.views import (
    PlaceView,
    PlaceImageView
)
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):
    def get(self, request):
        return Response({
            'message': 'Welcome to StayWise Places API',
            'endpoints': [
                '/places/',
                '/place-images/'
            ]
        })

router = SimpleRouter()
router.register('places', PlaceView, basename='places')
router.register('place-images', PlaceImageView, basename='place-images')

urlpatterns = [
    path('', HomeView.as_view()),
] + router.urls