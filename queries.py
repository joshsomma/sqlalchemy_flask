from actors import Actor
from main import Base, Session
from contact_details import ContactDetails
from movie import Movie
from datetime import date

session = Session()

all_movies = session.query(Movie).all()

print('\n### All movies')
for movie in all_movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('')

# get movies after 15-01-01
recent_movies = session.query(Movie).filter(Movie.release_date > date(2015,1,1)).all()

print('\n### Recent movies')
for movie in recent_movies:
    print(f'{movie.title} was released on {movie.release_date}')
print('')

# movies with the rock!
rock_movies = session.query(Movie).join(Actor, Movie.actors).filter(Actor.name == 'Dwayne Johnson').all()

print('\n### Rock movies')
for movie in rock_movies:
    print(f'The Rock starred in {movie.title}')
print('')

# actors from Glendale
glendale_actors = session.query(Actor).join(ContactDetails).filter(ContactDetails.address.ilike('%glendale%')).all()

print('\n### actors from glendale')
for actor in glendale_actors:
    print(f'{actor.name} has a house in Glendale')
print('')