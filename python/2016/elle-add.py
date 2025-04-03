
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Elle to the database
movies.insert(
    title="Elle", 
    year=2016, 
    plot="A successful businesswoman gets caught up in a game of cat and mouse as she tracks down the unknown man who raped her.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Elle", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    