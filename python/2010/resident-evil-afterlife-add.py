
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Resident Evil: Afterlife to the database
movies.insert(
    title="Resident Evil: Afterlife", 
    year=2010, 
    plot="While still out to destroy the evil Umbrella Corporation, Alice joins a group of survivors living in a prison surrounded by the infected who also want to relocate to the mysterious but supposedly unharmed safe haven known only as Arcadia.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Resident Evil: Afterlife", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    