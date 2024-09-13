from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="GetVilla API",
        default_version='v1',
        description="A temparory API documentation for GetVilla API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


class HomeView(APIView):
    def get(self, request):
        return Response({
            'message': 'Welcome to GetVilla API',
            'endpoints': [
                '/csc/',
                '/places/',
                '/users/',
            ]
        })


urlpatterns = [
    path("", HomeView.as_view()),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("places/", include("places.urls")),
    path("csc/", include("csc.urls")),
]