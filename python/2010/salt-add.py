
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Salt to the database
movies.insert(
    title="Salt", 
    year=2010, 
    plot="A CIA agent goes on the run after a defector accuses her of being a Russian spy.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Salt", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    