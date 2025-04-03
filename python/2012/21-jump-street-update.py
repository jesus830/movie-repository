
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="21 Jump Street", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="21 Jump Street", 
        year=2012, 
        plot="A pair of underachieving cops are sent back to a local high school to blend in and bring down a synthetic drug ring.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    