
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Bonjour Anne to the database
movies.insert(
    title="Bonjour Anne", 
    year=2016, 
    plot="Anne is at a crossroads in her life. Long married to a successful, driven but inattentive movie producer, she unexpectedly finds herself taking a car trip from Cannes to Paris with a ... See full summary »", 
    rating=4.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Bonjour Anne", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    