
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Scott Pilgrim vs. the World to the database
movies.insert(
    title="Scott Pilgrim vs. the World", 
    year=2010, 
    plot="Scott Pilgrim must defeat his new girlfriend's seven evil exes in order to win her heart.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Scott Pilgrim vs. the World", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    