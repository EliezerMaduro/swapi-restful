from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.rest_api.views import (
    PlanetViewSet, FilmViewSet, SpeciesViewSet,
    StarshipViewSet, VehicleViewSet, PersonViewSet
)

router = DefaultRouter()
router.register(r'planets', PlanetViewSet, basename='planet')
router.register(r'films', FilmViewSet, basename='film')
router.register(r'species', SpeciesViewSet, basename='species')
router.register(r'starships', StarshipViewSet, basename='starship')
router.register(r'vehicles', VehicleViewSet, basename='vehicle')
router.register(r'people', PersonViewSet, basename='person')

urlpatterns = [
    path('', include(router.urls)),
]