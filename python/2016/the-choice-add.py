
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Choice to the database
movies.insert(
    title="The Choice", 
    year=2016, 
    plot="Travis and Gabby first meet as neighbors in a small coastal town and wind up in a relationship that is tested by life's most defining events.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Choice", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    