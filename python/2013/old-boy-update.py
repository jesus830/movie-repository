
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Old Boy", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Old Boy", 
        year=2013, 
        plot="Obsessed with vengeance, a man sets out to find out why he was kidnapped and locked into solitary confinement for twenty years without reason.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    