
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Star Trek to the database
movies.insert(
    title="Star Trek", 
    year=2009, 
    plot="The brash James T. Kirk tries to live up to his father's legacy with Mr. Spock keeping him in check as a vengeful Romulan from the future creates black holes to destroy the Federation one planet at a time.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="Star Trek", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    