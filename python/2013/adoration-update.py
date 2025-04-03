
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Adoration", 
    year=2013
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Adoration", 
        year=2013, 
        plot="A pair of childhood friends and neighbors fall for each other's sons.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    