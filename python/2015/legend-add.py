
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Legend to the database
movies.insert(
    title="Legend", 
    year=2015, 
    plot="Identical twin gangsters Ronald and Reginald Kray terrorize London during the 1960s.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Legend", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    