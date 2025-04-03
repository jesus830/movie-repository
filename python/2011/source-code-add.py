
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Source Code to the database
movies.insert(
    title="Source Code", 
    year=2011, 
    plot="A soldier wakes up in someone else's body and discovers he's part of an experimental government program to find the bomber of a commuter train. A mission he has only 8 minutes to complete.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Source Code", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    