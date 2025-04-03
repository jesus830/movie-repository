
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Genius to the database
movies.insert(
    title="Genius", 
    year=2016, 
    plot="A chronicle of Max Perkins's time as the book editor at Scribner, where he oversaw works by Thomas Wolfe, Ernest Hemingway, F. Scott Fitzgerald and others.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Genius", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    