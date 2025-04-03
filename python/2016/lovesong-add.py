
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Lovesong to the database
movies.insert(
    title="Lovesong", 
    year=2016, 
    plot="The relationship between two friends deepens during an impromptu road trip.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Lovesong", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    