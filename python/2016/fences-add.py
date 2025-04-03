
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Fences to the database
movies.insert(
    title="Fences", 
    year=2016, 
    plot="A working-class African-American father tries to raise his family in the 1950s, while coming to terms with the events of his life.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Fences", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    