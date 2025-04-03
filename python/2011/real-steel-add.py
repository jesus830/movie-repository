
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Real Steel to the database
movies.insert(
    title="Real Steel", 
    year=2011, 
    plot="In the near future, robot boxing is a top sport. A struggling promoter feels he's found a champion in a discarded robot.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Real Steel", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    