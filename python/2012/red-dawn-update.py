
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Red Dawn", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Red Dawn", 
        year=2012, 
        plot="A group of teenagers look to save their town from an invasion of North Korean soldiers.", 
        rating=5.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    