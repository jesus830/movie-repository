
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Daughter to the database
movies.insert(
    title="The Daughter", 
    year=2015, 
    plot="The story follows a man who returns home to discover a long-buried family secret, and whose attempts to put things right threaten the lives of those he left home years before.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Daughter", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    