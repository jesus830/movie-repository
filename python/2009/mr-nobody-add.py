
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mr. Nobody to the database
movies.insert(
    title="Mr. Nobody", 
    year=2009, 
    plot="A boy stands on a station platform as a train is about to leave. Should he go with his mother or stay with his father? Infinite possibilities arise from this decision. As long as he doesn't choose, anything is possible.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Mr. Nobody", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    