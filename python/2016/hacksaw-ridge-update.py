
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Hacksaw Ridge", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Hacksaw Ridge", 
        year=2016, 
        plot="WWII American Army Medic Desmond T. Doss, who served during the Battle of Okinawa, refuses to kill people, and becomes the first man in American history to receive the Medal of Honor without firing a shot.", 
        rating=8.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    