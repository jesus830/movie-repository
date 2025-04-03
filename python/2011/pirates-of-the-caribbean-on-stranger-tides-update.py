
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Pirates of the Caribbean: On Stranger Tides", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Pirates of the Caribbean: On Stranger Tides", 
        year=2011, 
        plot="Jack Sparrow and Barbossa embark on a quest to find the elusive fountain of youth, only to discover that Blackbeard and his daughter are after it too.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    