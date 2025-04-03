
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Lego Movie to the database
movies.insert(
    title="The Lego Movie", 
    year=2014, 
    plot="An ordinary Lego construction worker, thought to be the prophesied 'Special', is recruited to join a quest to stop an evil tyrant from gluing the Lego universe into eternal stasis.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Lego Movie", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    