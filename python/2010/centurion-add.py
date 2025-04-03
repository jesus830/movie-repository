
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Centurion to the database
movies.insert(
    title="Centurion", 
    year=2010, 
    plot="A splinter group of Roman soldiers fight for their lives behind enemy lines after their legion is decimated in a devastating guerrilla attack.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Centurion", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    