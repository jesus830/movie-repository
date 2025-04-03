
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sunshine to the database
movies.insert(
    title="Sunshine", 
    year=2007, 
    plot="A team of international astronauts are sent on a dangerous mission to reignite the dying Sun with a nuclear fission bomb in 2057.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Sunshine", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    