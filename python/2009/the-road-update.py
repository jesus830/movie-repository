
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Road", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Road", 
        year=2009, 
        plot="In a dangerous post-apocalyptic world, an ailing father defends his son as they slowly travel to the sea.", 
        rating=7.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    