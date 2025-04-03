
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="It Follows", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="It Follows", 
        year=2014, 
        plot="A young woman is followed by an unknown supernatural force after a sexual encounter.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    