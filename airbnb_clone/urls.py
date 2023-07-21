from django.contrib import admin
from django.urls import path, include
from .app.views import CountryViewSet, StateViewSet, VillageViewSet, ViewsViewSet, PlaceViewSet, ReservationViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'states', StateViewSet)
router.register(r'villages', VillageViewSet)
router.register(r'views', ViewsViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
