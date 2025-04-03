
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Disappointments Room to the database
movies.insert(
    title="The Disappointments Room", 
    year=2016, 
    plot="A mother and her young son release unimaginable horrors from the attic of their rural dream home.", 
    rating=3.9
)

# Confirm that the movie was added
movie = movies.select(
    title="The Disappointments Room", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    