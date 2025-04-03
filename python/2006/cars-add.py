
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Cars to the database
movies.insert(
    title="Cars", 
    year=2006, 
    plot="A hot-shot race-car named Lightning McQueen gets waylaid in Radiator Springs, where he finds the true meaning of friendship and family.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Cars", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    