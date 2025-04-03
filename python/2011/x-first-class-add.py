
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add X: First Class to the database
movies.insert(
    title="X: First Class", 
    year=2011, 
    plot="In 1962, the United States government enlists the help of Mutants with superhuman abilities to stop a malicious dictator who is determined to start World War III.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="X: First Class", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    