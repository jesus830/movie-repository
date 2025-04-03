
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Funny Games to the database
movies.insert(
    title="Funny Games", 
    year=2007, 
    plot="Two psychopathic young men take a family hostage in their cabin.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Funny Games", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    