
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Max Steel to the database
movies.insert(
    title="Max Steel", 
    year=2016, 
    plot="The adventures of teenager Max McGrath and his alien companion, Steel, who must harness and combine their tremendous new powers to evolve into the turbo-charged superhero Max Steel.", 
    rating=4.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Max Steel", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    