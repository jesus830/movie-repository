
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Clown", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Clown", 
        year=2014, 
        plot="A loving father finds a clown suit for his son's birthday party, only to realize that it is not a suit at all.", 
        rating=5.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    