
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Revolutionary Road to the database
movies.insert(
    title="Revolutionary Road", 
    year=2008, 
    plot="A young couple living in a Connecticut suburb during the mid-1950s struggle to come to terms with their personal problems while trying to raise their two children.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Revolutionary Road", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    