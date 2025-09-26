from rest_framework.viewsets import ModelViewSet
from apps.core.models import Planet, Film, Species, Starship, Vehicle, Person
from apps.rest_api.serializers import (
    PlanetSerializer, FilmSerializer, SpeciesSerializer,
    StarshipSerializer, VehicleSerializer, PersonSerializer
)

class PlanetViewSet(ModelViewSet):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class SpeciesViewSet(ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

class StarshipViewSet(ModelViewSet):
    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer

class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer