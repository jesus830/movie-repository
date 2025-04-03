
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Transformers: Dark of the Moon to the database
movies.insert(
    title="Transformers: Dark of the Moon", 
    year=2011, 
    plot="The Autobots learn of a Cybertronian spacecraft hidden on the moon, and race against the Decepticons to reach it and to learn its secrets.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Transformers: Dark of the Moon", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    