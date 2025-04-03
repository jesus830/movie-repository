
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Money Monster to the database
movies.insert(
    title="Money Monster", 
    year=2016, 
    plot="Financial TV host Lee Gates and his producer Patty are put in an extreme situation when an irate investor takes over their studio.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Money Monster", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    