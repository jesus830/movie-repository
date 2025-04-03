
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="That Awkward Moment", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="That Awkward Moment", 
        year=2014, 
        plot="Three best friends find themselves where we've all been - at that confusing moment in every dating relationship when you have to decide "So...where is this going?"", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    