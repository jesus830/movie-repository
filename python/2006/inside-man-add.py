
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Inside Man to the database
movies.insert(
    title="Inside Man", 
    year=2006, 
    plot="A police detective, a bank robber, and a high-power broker enter high-stakes negotiations after the criminal's brilliant heist spirals into a hostage situation.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Inside Man", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    