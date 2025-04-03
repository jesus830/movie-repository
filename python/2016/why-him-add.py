
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Why Him? to the database
movies.insert(
    title="Why Him?", 
    year=2016, 
    plot="A holiday gathering threatens to go off the rails when Ned Fleming realizes that his daughter's Silicon Valley millionaire boyfriend is about to pop the question.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Why Him?", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    