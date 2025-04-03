
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hairspray to the database
movies.insert(
    title="Hairspray", 
    year=2007, 
    plot="Pleasantly plump teenager Tracy Turnblad teaches 1962 Baltimore a thing or two about integration after landing a spot on a local TV dance show.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Hairspray", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    