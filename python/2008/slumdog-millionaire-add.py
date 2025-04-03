
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Slumdog Millionaire to the database
movies.insert(
    title="Slumdog Millionaire", 
    year=2008, 
    plot="A Mumbai teen reflects on his upbringing in the slums when he is accused of cheating on the Indian Version of "Who Wants to be a Millionaire?"", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="Slumdog Millionaire", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    