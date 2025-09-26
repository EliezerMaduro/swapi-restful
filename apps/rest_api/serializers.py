from rest_framework import serializers
from apps.core.models import Planet, Film, Species, Starship, Vehicle, Person

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ['id', 'name', 'diameter', 'climates', 'population', 'created', 'edited']

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title', 'episode_id', 'release_date', 'director', 'created', 'edited']

class SpeciesSerializer(serializers.ModelSerializer):
    homeworld = serializers.PrimaryKeyRelatedField(queryset=Planet.objects.all(), allow_null=True)
    people = serializers.PrimaryKeyRelatedField(many=True, queryset=Person.objects.all())
    films = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all())
    homeworld_name = serializers.CharField(source='homeworld.name', read_only=True)

    class Meta:
        model = Species
        fields = [
            'id', 'name', 'classification', 'designation', 'average_height',
            'average_lifespan', 'homeworld', 'homeworld_name', 'people', 'films',
            'created', 'edited'
        ]

class StarshipSerializer(serializers.ModelSerializer):
    pilots = serializers.PrimaryKeyRelatedField(many=True, queryset=Person.objects.all())
    films = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all())

    class Meta:
        model = Starship
        fields = [
            'id', 'name', 'model', 'manufacturers', 'hyperdrive_rating',
            'crew', 'passengers', 'pilots', 'films', 'created', 'edited'
        ]

class VehicleSerializer(serializers.ModelSerializer):
    pilots = serializers.PrimaryKeyRelatedField(many=True, queryset=Person.objects.all())
    films = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all())

    class Meta:
        model = Vehicle
        fields = [
            'id', 'name', 'model', 'manufacturers', 'crew', 'passengers',
            'pilots', 'films', 'created', 'edited'
        ]

class PersonSerializer(serializers.ModelSerializer):
    homeworld = serializers.PrimaryKeyRelatedField(queryset=Planet.objects.all(), allow_null=True)
    species = serializers.PrimaryKeyRelatedField(many=True, queryset=Species.objects.all())
    films = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all())
    homeworld_name = serializers.CharField(source='homeworld.name', read_only=True)

    class Meta:
        model = Person
        fields = [
            'id', 'name', 'height', 'mass', 'gender', 'homeworld', 'homeworld_name',
            'species', 'films', 'created', 'edited'
        ]