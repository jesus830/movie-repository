
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add No Strings Attached to the database
movies.insert(
    title="No Strings Attached", 
    year=2011, 
    plot="A guy and girl try to keep their relationship strictly physical, but it's not long before they learn that they want something more.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="No Strings Attached", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    