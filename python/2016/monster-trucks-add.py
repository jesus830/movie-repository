
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Monster Trucks to the database
movies.insert(
    title="Monster Trucks", 
    year=2016, 
    plot="A young man working at a small town junkyard discovers and befriends a creature which feeds on oil being sought by a fracking company.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Monster Trucks", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    