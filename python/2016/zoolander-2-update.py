
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Zoolander 2", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Zoolander 2", 
        year=2016, 
        plot="Derek and Hansel are lured into modeling again, in Rome, where they find themselves the target of a sinister conspiracy.", 
        rating=4.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    