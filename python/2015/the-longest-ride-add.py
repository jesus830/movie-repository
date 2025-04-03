
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Longest Ride to the database
movies.insert(
    title="The Longest Ride", 
    year=2015, 
    plot="The lives of a young couple intertwine with a much older man, as he reflects back on a past love.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Longest Ride", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    