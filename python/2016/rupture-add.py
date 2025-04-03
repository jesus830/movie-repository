
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Rupture to the database
movies.insert(
    title="Rupture", 
    year=2016, 
    plot="A single mom tries to break free from a mysterious organization that has abducted her.", 
    rating=4.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Rupture", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    