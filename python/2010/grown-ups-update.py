
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Grown Ups", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Grown Ups", 
        year=2010, 
        plot="After their high school basketball coach passes away, five good friends and former teammates reunite for a Fourth of July holiday weekend.", 
        rating=6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    