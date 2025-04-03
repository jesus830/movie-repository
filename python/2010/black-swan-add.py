
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Black Swan to the database
movies.insert(
    title="Black Swan", 
    year=2010, 
    plot="A committed dancer wins the lead role in a production of Tchaikovsky's "Swan Lake" only to find herself struggling to maintain her sanity.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="Black Swan", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    