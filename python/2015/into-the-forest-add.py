
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Into the Forest to the database
movies.insert(
    title="Into the Forest", 
    year=2015, 
    plot="After a massive power outage, two sisters learn to survive on their own in their isolated woodland home.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Into the Forest", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    