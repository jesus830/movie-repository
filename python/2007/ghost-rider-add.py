
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Ghost Rider to the database
movies.insert(
    title="Ghost Rider", 
    year=2007, 
    plot="Stunt motorcyclist Johnny Blaze gives up his soul to become a hellblazing vigilante, to fight against power hungry Blackheart, the son of the devil himself.", 
    rating=5.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Ghost Rider", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    