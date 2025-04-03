
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 22 Jump Street to the database
movies.insert(
    title="22 Jump Street", 
    year=2014, 
    plot="After making their way through high school (twice), big changes are in store for officers Schmidt and Jenko when they go deep undercover at a local college.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="22 Jump Street", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    