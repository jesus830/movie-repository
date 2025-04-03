
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hacksaw Ridge to the database
movies.insert(
    title="Hacksaw Ridge", 
    year=2016, 
    plot="WWII American Army Medic Desmond T. Doss, who served during the Battle of Okinawa, refuses to kill people, and becomes the first man in American history to receive the Medal of Honor without firing a shot.", 
    rating=8.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Hacksaw Ridge", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    