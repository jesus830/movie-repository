
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The First Time to the database
movies.insert(
    title="The First Time", 
    year=2012, 
    plot="A shy senior and a down-to-earth junior fall in love over one weekend.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="The First Time", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    