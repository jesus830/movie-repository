
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Transformers: Dark of the Moon", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Transformers: Dark of the Moon", 
        year=2011, 
        plot="The Autobots learn of a Cybertronian spacecraft hidden on the moon, and race against the Decepticons to reach it and to learn its secrets.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    