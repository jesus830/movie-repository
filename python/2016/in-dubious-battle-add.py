
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add In Dubious Battle to the database
movies.insert(
    title="In Dubious Battle", 
    year=2016, 
    plot="An activist gets caught up in the labor movement for farm workers in California during the 1930s.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="In Dubious Battle", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    