
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Warriors Gate to the database
movies.insert(
    title="The Warriors Gate", 
    year=2016, 
    plot="A teenager is magically transported to China and learns to convert his video game skills into those of a Kung Fu warrior.", 
    rating=5.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Warriors Gate", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    