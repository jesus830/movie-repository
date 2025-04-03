
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Book of Life to the database
movies.insert(
    title="The Book of Life", 
    year=2014, 
    plot="Manolo, a young man who is torn between fulfilling the expectations of his family and following his heart, embarks on an adventure that spans three fantastic worlds where he must face his greatest fears.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Book of Life", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    