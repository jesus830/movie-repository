
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Super 8 to the database
movies.insert(
    title="Super 8", 
    year=2011, 
    plot="During the summer of 1979, a group of friends witness a train crash and investigate subsequent unexplained events in their small town.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Super 8", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    