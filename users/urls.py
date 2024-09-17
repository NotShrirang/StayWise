from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.views import APIView
from rest_framework.response import Response
from users.views import (
    StayWiseUserView,
    StayWiseUserRegisterView,
    StayWiseUserLoginView,
    StayWiseUserLogoutView,
    ReservationUserView,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView
)


class HomeView(APIView):
    def get(self, request):
        return Response({
            'message': 'Welcome to StayWise Users API',
            'endpoints': [
                '/login/',
                '/register/',
                '/logout/',
                '/token/refresh/',
                '/users/',
                '/reservation-users/',
            ]
        })


router = SimpleRouter()
router.register(r'users', StayWiseUserView, basename='users')
router.register(r'reservation-users', ReservationUserView, basename='reservation-users')

urlpatterns = [
    path('', HomeView.as_view(), name="homeview"),
    path('register/', StayWiseUserRegisterView.as_view(), name="register"),
    path('login/', StayWiseUserLoginView.as_view(), name="login"),
    path('logout/', StayWiseUserLogoutView.as_view(), name="logout"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls