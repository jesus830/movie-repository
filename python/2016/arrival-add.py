
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Arrival to the database
movies.insert(
    title="Arrival", 
    year=2016, 
    plot="When twelve mysterious spacecraft appear around the world, linguistics professor Louise Banks is tasked with interpreting the language of the apparent alien visitors.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="Arrival", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    