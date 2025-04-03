
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Twilight to the database
movies.insert(
    title="Twilight", 
    year=2008, 
    plot="A teenage girl risks everything when she falls in love with a vampire.", 
    rating=5.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Twilight", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    