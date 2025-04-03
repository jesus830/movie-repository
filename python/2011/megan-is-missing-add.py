
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Megan Is Missing to the database
movies.insert(
    title="Megan Is Missing", 
    year=2011, 
    plot="Two teenage girls encounter an Internet child predator.", 
    rating=4.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Megan Is Missing", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    