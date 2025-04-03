
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Vincent N Roxxy to the database
movies.insert(
    title="Vincent N Roxxy", 
    year=2016, 
    plot="A small town loner and a rebellious punk rocker unexpectedly fall in love as they are forced on the run and soon discover violence follows them everywhere.", 
    rating=5.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Vincent N Roxxy", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    