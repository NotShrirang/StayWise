from csc.views import (
    CityView,
    StateView,
    CountryView
)
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.views import APIView
from rest_framework.response import Response

class HomeView(APIView):
    def get(self, request):
        return Response({
            'message': 'Welcome to StayWise CSC (City State Country) API',
            'endpoints': [
                '/city/',
                '/state/',
                '/country/',
            ]
        })

router = SimpleRouter()
router.register('city', CityView, basename='city')
router.register('state', StateView, basename='state')
router.register('country', CountryView, basename='country')

urlpatterns = [
    path('', HomeView.as_view()),
] + router.urls