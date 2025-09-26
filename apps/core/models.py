from django.db import models

class Planet(models.Model):
    id = models.CharField(max_length=100, primary_key=True) 
    name = models.CharField(max_length=100) 
    diameter = models.CharField(max_length=50, null=True, blank=True)
    climates = models.CharField(max_length=200, null=True, blank=True)
    population = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    edited = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['id'])]

    def __str__(self):
        return self.name

class Film(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100) 
    episode_id = models.IntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    director = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    edited = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['id'])]

    def __str__(self):
        return self.title

class Species(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    classification = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    average_height = models.CharField(max_length=50, null=True, blank=True)
    average_lifespan = models.CharField(max_length=50, null=True, blank=True)
    homeworld = models.ForeignKey('Planet', on_delete=models.SET_NULL, null=True, blank=True)
    people = models.ManyToManyField('Person', blank=True, related_name='species_set')
    films = models.ManyToManyField('Film', blank=True, related_name='species')
    created = models.DateTimeField(null=True, blank=True)
    edited = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['id'])]

    def __str__(self):
        return self.name

class Starship(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100, null=True, blank=True)
    manufacturers = models.CharField(max_length=200, null=True, blank=True)
    hyperdrive_rating = models.CharField(max_length=50, null=True, blank=True)
    crew = models.CharField(max_length=50, null=True, blank=True)
    passengers = models.CharField(max_length=50, null=True, blank=True)
    pilots = models.ManyToManyField('Person', blank=True, related_name='starships')
    films = models.ManyToManyField('Film', blank=True, related_name='starships')
    created = models.DateTimeField(null=True, blank=True)
    edited = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['id'])]

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100, null=True, blank=True)
    manufacturers = models.CharField(max_length=200, null=True, blank=True)
    crew = models.CharField(max_length=50, null=True, blank=True)
    passengers = models.CharField(max_length=50, null=True, blank=True)
    pilots = models.ManyToManyField('Person', blank=True, related_name='vehicles')
    films = models.ManyToManyField('Film', blank=True, related_name='vehicles')
    created = models.DateTimeField(null=True, blank=True)
    edited = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['id'])]

    def __str__(self):
        return self.name

class Person(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    height = models.CharField(max_length=50, null=True, blank=True)
    mass = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    homeworld = models.ForeignKey('Planet', on_delete=models.SET_NULL, null=True, blank=True)
    species = models.ManyToManyField('Species', blank=True, related_name='members')
    films = models.ManyToManyField('Film', blank=True, related_name='characters')
    created = models.DateTimeField(null=True, blank=True)
    edited = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [models.Index(fields=['id'])]

    def __str__(self):
        return self.name