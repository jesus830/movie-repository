
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Secret Scripture", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Secret Scripture", 
        year=2016, 
        plot="A woman keeps a diary of her extended stay at a mental hospital.", 
        rating=6.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    