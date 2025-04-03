
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Slither", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Slither", 
        year=2006, 
        plot="A small town is taken over by an alien plague, turning residents into zombies and all forms of mutant monsters.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    