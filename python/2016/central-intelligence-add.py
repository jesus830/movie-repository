
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Central Intelligence to the database
movies.insert(
    title="Central Intelligence", 
    year=2016, 
    plot="After he reconnects with an awkward pal from high school through Facebook, a mild-mannered accountant is lured into the world of international espionage.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Central Intelligence", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    