
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Ghost Rider", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Ghost Rider", 
        year=2007, 
        plot="Stunt motorcyclist Johnny Blaze gives up his soul to become a hellblazing vigilante, to fight against power hungry Blackheart, the son of the devil himself.", 
        rating=5.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    