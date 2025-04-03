
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Bonjour Anne", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Bonjour Anne", 
        year=2016, 
        plot="Anne is at a crossroads in her life. Long married to a successful, driven but inattentive movie producer, she unexpectedly finds herself taking a car trip from Cannes to Paris with a ... See full summary »", 
        rating=4.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    