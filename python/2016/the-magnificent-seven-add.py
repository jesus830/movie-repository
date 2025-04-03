
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Magnificent Seven to the database
movies.insert(
    title="The Magnificent Seven", 
    year=2016, 
    plot="Seven gunmen in the old west gradually come together to help a poor village against savage thieves.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="The Magnificent Seven", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    