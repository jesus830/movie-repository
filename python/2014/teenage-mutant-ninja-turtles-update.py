
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Teenage Mutant Ninja Turtles", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Teenage Mutant Ninja Turtles", 
        year=2014, 
        plot="When a kingpin threatens New York City, a group of mutated turtle warriors must emerge from the shadows to protect their home.", 
        rating=5.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    