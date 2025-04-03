
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 21 Jump Street to the database
movies.insert(
    title="21 Jump Street", 
    year=2012, 
    plot="A pair of underachieving cops are sent back to a local high school to blend in and bring down a synthetic drug ring.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="21 Jump Street", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    