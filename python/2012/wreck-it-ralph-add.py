
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Wreck-It Ralph to the database
movies.insert(
    title="Wreck-It Ralph", 
    year=2012, 
    plot="A video game villain wants to be a hero and sets out to fulfill his dream, but his quest brings havoc to the whole arcade where he lives.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Wreck-It Ralph", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    