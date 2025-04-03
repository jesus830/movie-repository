
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Hollars to the database
movies.insert(
    title="The Hollars", 
    year=2016, 
    plot="A man returns to his small hometown after learning that his mother has fallen ill and is about to undergo surgery.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Hollars", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    