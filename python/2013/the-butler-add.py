
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Butler to the database
movies.insert(
    title="The Butler", 
    year=2013, 
    plot="As Cecil Gaines serves eight presidents during his tenure as a butler at the White House, the civil rights movement, Vietnam, and other major events affect this man's life, family, and American society.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Butler", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    