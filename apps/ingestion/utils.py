from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from apps.core.models import Person, Film, Planet, Species, Starship, Vehicle
from datetime import datetime
import iso8601
import logging

logger = logging.getLogger(__name__)

def query_graphql(endpoint, query_str):
    transport = RequestsHTTPTransport(url=endpoint, verify=True, retries=3)
    client = Client(transport=transport)
    query = gql(query_str)
    try:
        return client.execute(query)
    except Exception as e:
        logger.error(f"Error querying GraphQL API: {e}")
        raise

def fetch_swapi_data():
    endpoint = "https://swapi-graphql.netlify.app/graphql"
    query = """
        query GetAllData {
            allPlanets {
                planets {
                name
                diameter
                climates
                population
                created
                edited
                id
                }
            }
            allSpecies {
                species {
                id
                name
                classification
                designation
                averageHeight
                averageLifespan
                homeworld {
                    name
                }
                created
                edited
                personConnection {
                    people {
                    name
                    }
                }
                filmConnection {
                    films {
                    title
                    }
                }
                }
            }
            allStarships {
                starships {
                id
                name
                model
                manufacturers
                hyperdriveRating
                crew
                passengers
                created
                edited
                pilotConnection {
                    pilots {
                    name
                    }
                }
                filmConnection {
                    films {
                    title
                    }
                }
                }
            }
            allVehicles {
                vehicles {
                id
                name
                model
                manufacturers
                crew
                passengers
                pilotConnection {
                    pilots {
                    name
                    }
                }
                filmConnection {
                    films {
                    title
                    }
                }
                created
                edited
                }
            }
            allPeople {
                people {
                id
                name
                height
                mass
                gender
                homeworld {
                    name
                }
                species {
                    name
                }
                filmConnection {
                    films {
                    title
                    }
                }
                created
                edited
                }
            }
            allFilms {
                films {
                id
                title
                episodeID
                releaseDate
                director
                created
                edited
                }
            }
        }
    """
    logger.info("Fetching data from SWAPI GraphQL API")
    return query_graphql(endpoint, query)

def save_deltas(data):
    logger.info("Starting data ingestion for SWAPI")
    try:
        save_planets(data['allPlanets']['planets'])

        save_films(data['allFilms']['films'])

        save_species(data['allSpecies']['species'])
        
        save_starships(data['allStarships']['starships'])

        save_vehicles(data['allVehicles']['vehicles'])

        save_people(data['allPeople']['people'])
        
        logger.info("Completed data ingestion for SWAPI")
        
    except Exception as e:
        logger.error(f"Error saving data: {e}")
        raise
    
def save_planets(data):
    for planet_data in data:
        Planet.objects.update_or_create(
            id=planet_data['id'],
            defaults={
                'name': planet_data['name'],
                'diameter': planet_data['diameter'],
                'climates': planet_data['climates'],
                'population': planet_data['population'],
                'created': iso8601.parse_date(planet_data['created']) if planet_data['created'] else None,
                'edited': iso8601.parse_date(planet_data['edited']) if planet_data['edited'] else None,
            }
        )
        
def save_films(data):
    for film_data in data:
        Film.objects.update_or_create(
            id=film_data['id'],
            defaults={
                'title': film_data['title'],
                'episode_id': film_data['episodeID'],
                'release_date': film_data['releaseDate'],
                'director': film_data['director'],
                'created': iso8601.parse_date(film_data['created']) if film_data['created'] else None,
                'edited': iso8601.parse_date(film_data['edited']) if film_data['edited'] else None,
            }
        )
        
def save_species(data):
    for species_data in data:
        homeworld = Planet.objects.filter(name=species_data['homeworld']['name']).first() if species_data['homeworld'] else None
        species, _ = Species.objects.update_or_create(
            id=species_data['id'],
            defaults={
                'name': species_data['name'],
                'classification': species_data['classification'],
                'designation': species_data['designation'],
                'average_height': species_data['averageHeight'],
                'average_lifespan': species_data['averageLifespan'],
                'homeworld': homeworld,
                'created': iso8601.parse_date(species_data['created']) if species_data['created'] else None,
                'edited': iso8601.parse_date(species_data['edited']) if species_data['edited'] else None,
            }
        )
        # Assign many-to-many relationships
        if species_data['personConnection']['people']:
            people = Person.objects.filter(name__in=[p['name'] for p in species_data['personConnection']['people']])
            species.people.set(people)
        if species_data['filmConnection']['films']:
            films = Film.objects.filter(title__in=[f['title'] for f in species_data['filmConnection']['films']])
            species.films.set(films)
            
def save_starships(data):
    for starship_data in data:
        starship, _ = Starship.objects.update_or_create(
            id=starship_data['id'],
            defaults={
                'name': starship_data['name'],
                'model': starship_data['model'],
                'manufacturers': starship_data['manufacturers'],
                'hyperdrive_rating': starship_data['hyperdriveRating'],
                'crew': starship_data['crew'],
                'passengers': starship_data['passengers'],
                'created': iso8601.parse_date(starship_data['created']) if starship_data['created'] else None,
                'edited': iso8601.parse_date(starship_data['edited']) if starship_data['edited'] else None,
            }
        )
        # Assign many-to-many relationships
        if starship_data['pilotConnection']['pilots']:
            pilots = Person.objects.filter(name__in=[p['name'] for p in starship_data['pilotConnection']['pilots']])
            starship.pilots.set(pilots)
        if starship_data['filmConnection']['films']:
            films = Film.objects.filter(title__in=[f['title'] for f in starship_data['filmConnection']['films']])
            starship.films.set(films)
            
def save_vehicles(data):
    for vehicle_data in data:
        vehicle, _ = Vehicle.objects.update_or_create(
            id=vehicle_data['id'],
            defaults={
                'name': vehicle_data['name'],
                'model': vehicle_data['model'],
                'manufacturers': vehicle_data['manufacturers'],
                'crew': vehicle_data['crew'],
                'passengers': vehicle_data['passengers'],
                'created': iso8601.parse_date(vehicle_data['created']) if vehicle_data['created'] else None,
                'edited': iso8601.parse_date(vehicle_data['edited']) if vehicle_data['edited'] else None,
            }
        )
        # Assign many-to-many relationships
        if vehicle_data['pilotConnection']['pilots']:
            pilots = Person.objects.filter(name__in=[p['name'] for p in vehicle_data['pilotConnection']['pilots']])
            vehicle.pilots.set(pilots)
        if vehicle_data['filmConnection']['films']:
            films = Film.objects.filter(title__in=[f['title'] for f in vehicle_data['filmConnection']['films']])
            vehicle.films.set(films)
            
def save_people(data):
    for person_data in data:
        homeworld = Planet.objects.filter(name=person_data['homeworld']['name']).first() if person_data['homeworld'] else None
        person, _ = Person.objects.update_or_create(
            id=person_data['id'],
            defaults={
                'name': person_data['name'],
                'height': person_data['height'],
                'mass': person_data['mass'],
                'gender': person_data['gender'],
                'homeworld': homeworld,
                'created': iso8601.parse_date(person_data['created']) if person_data['created'] else None,
                'edited': iso8601.parse_date(person_data['edited']) if person_data['edited'] else None,
            }
        )
        # Assign many-to-many relationships
        if person_data['filmConnection']['films']:
            films = Film.objects.filter(title__in=[f['title'] for f in person_data['filmConnection']['films']])
            person.films.set(films)
        if person_data['species']:
            species = Species.objects.filter(name__in=[s['name'] for s in person_data['species']])
            person.species.set(species)