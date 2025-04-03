
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mommy to the database
movies.insert(
    title="Mommy", 
    year=2014, 
    plot="A widowed single mother, raising her violent son alone, finds new hope when a mysterious neighbor inserts herself into their household.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Mommy", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    