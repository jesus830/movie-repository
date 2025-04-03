
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Babel", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Babel", 
        year=2006, 
        plot="Tragedy strikes a married couple on vacation in the Moroccan desert, touching off an interlocking story involving four different families.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    