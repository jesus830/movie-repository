
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Never Back Down to the database
movies.insert(
    title="Never Back Down", 
    year=2008, 
    plot="A frustrated and conflicted teenager arrives at a new high school to discover an underground fight club and meet a classmate who begins to coerce him into fighting.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Never Back Down", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    