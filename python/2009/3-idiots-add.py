
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 3 Idiots to the database
movies.insert(
    title="3 Idiots", 
    year=2009, 
    plot="Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them "idiots".", 
    rating=8.4
)

# Confirm that the movie was added
movie = movies.select(
    title="3 Idiots", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    