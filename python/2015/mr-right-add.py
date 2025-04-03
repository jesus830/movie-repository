
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mr. Right to the database
movies.insert(
    title="Mr. Right", 
    year=2015, 
    plot="A girl falls for the "perfect" guy, who happens to have a very fatal flaw: he's a hitman on the run from the crime cartels who employ him.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Mr. Right", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    