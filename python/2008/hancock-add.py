
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hancock to the database
movies.insert(
    title="Hancock", 
    year=2008, 
    plot="Hancock is a superhero whose ill considered behavior regularly causes damage in the millions. He changes when the person he saves helps him improve his public image.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Hancock", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    