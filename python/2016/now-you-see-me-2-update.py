
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Now You See Me 2", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Now You See Me 2", 
        year=2016, 
        plot="The Four Horsemen resurface and are forcibly recruited by a tech genius to pull off their most impossible heist yet.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    