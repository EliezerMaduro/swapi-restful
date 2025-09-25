from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100, unique=True)
    diameter = models.CharField(max_length=50, null=True, blank=True)
    climate = models.CharField(max_length=100, null=True, blank=True)
    population = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    edited = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=100, unique=True)
    episode_id = models.IntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    director = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    edited = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['title'])]

    def __str__(self):
        return self.title

class Species(models.Model):
    name = models.CharField(max_length=100, unique=True)
    classification = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    average_height = models.CharField(max_length=50, null=True, blank=True)
    average_lifespan = models.CharField(max_length=50, null=True, blank=True)
    homeworld = models.ForeignKey(Planet, on_delete=models.SET_NULL, null=True, blank=True)
    people = models.ManyToManyField('Person', blank=True, related_name='species_set')  # Cambiado related_name
    films = models.ManyToManyField(Film, blank=True, related_name='species')
    created = models.DateTimeField(null=True, blank=True)
    edited = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name

class Starship(models.Model):
    name = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    hyperdrive_rating = models.CharField(max_length=50, null=True, blank=True)
    crew = models.CharField(max_length=50, null=True, blank=True)
    passengers = models.CharField(max_length=50, null=True, blank=True)
    pilots = models.ManyToManyField('Person', blank=True, related_name='starships')
    films = models.ManyToManyField(Film, blank=True, related_name='starships')
    created = models.DateTimeField(null=True, blank=True)
    edited = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=100, unique=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    crew = models.CharField(max_length=50, null=True, blank=True)
    passengers = models.CharField(max_length=50, null=True, blank=True)
    pilots = models.ManyToManyField('Person', blank=True, related_name='vehicles')
    films = models.ManyToManyField(Film, blank=True, related_name='vehicles')
    created = models.DateTimeField(null=True, blank=True)
    edited = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    height = models.CharField(max_length=50, null=True, blank=True)
    mass = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    homeworld = models.ForeignKey(Planet, on_delete=models.SET_NULL, null=True, blank=True)
    species = models.ManyToManyField(Species, blank=True, related_name='members')
    films = models.ManyToManyField(Film, blank=True, related_name='characters')
    created = models.DateTimeField(null=True, blank=True)
    edited = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['name'])]

    def __str__(self):
        return self.name