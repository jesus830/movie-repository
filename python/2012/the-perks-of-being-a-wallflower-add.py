
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Perks of Being a Wallflower to the database
movies.insert(
    title="The Perks of Being a Wallflower", 
    year=2012, 
    plot="An introvert freshman is taken under the wings of two seniors who welcome him to the real world.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Perks of Being a Wallflower", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    