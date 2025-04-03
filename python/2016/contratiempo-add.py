
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Contratiempo to the database
movies.insert(
    title="Contratiempo", 
    year=2016, 
    plot="A young businessman faces a lawyer trying to prove his innocence by the assassination of his lover.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Contratiempo", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    