
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 10 Years to the database
movies.insert(
    title="10 Years", 
    year=2011, 
    plot="The night before their high school reunion, a group of friends realize they still haven't quite grown up in some ways.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="10 Years", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    