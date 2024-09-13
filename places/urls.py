from places.views import (
    PlaceView
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
                '/places/'
            ]
        })

router = SimpleRouter()
router.register('places', PlaceView, basename='places')

urlpatterns = [
    path('', HomeView.as_view()),
] + router.urls