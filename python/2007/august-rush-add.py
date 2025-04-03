
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add August Rush to the database
movies.insert(
    title="August Rush", 
    year=2007, 
    plot="A drama with fairy tale elements, where an orphaned musical prodigy uses his gift as a clue to finding his birth parents.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="August Rush", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    