
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Let Me In to the database
movies.insert(
    title="Let Me In", 
    year=2010, 
    plot="A bullied young boy befriends a young female vampire who lives in secrecy with her guardian.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Let Me In", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    