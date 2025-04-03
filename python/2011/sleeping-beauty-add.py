
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sleeping Beauty to the database
movies.insert(
    title="Sleeping Beauty", 
    year=2011, 
    plot="A haunting portrait of Lucy, a young university student drawn into a mysterious hidden world of unspoken desires.", 
    rating=5.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Sleeping Beauty", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    