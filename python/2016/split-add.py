
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Split to the database
movies.insert(
    title="Split", 
    year=2016, 
    plot="Three girls are kidnapped by a man with a diagnosed 23 distinct personalities. They must try to escape before the apparent emergence of a frightful new 24th.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Split", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    