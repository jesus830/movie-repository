
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Trust to the database
movies.insert(
    title="Trust", 
    year=2010, 
    plot="A teenage girl is targeted by an online sexual predator.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Trust", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    