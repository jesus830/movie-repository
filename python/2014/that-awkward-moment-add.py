
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add That Awkward Moment to the database
movies.insert(
    title="That Awkward Moment", 
    year=2014, 
    plot="Three best friends find themselves where we've all been - at that confusing moment in every dating relationship when you have to decide "So...where is this going?"", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="That Awkward Moment", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    