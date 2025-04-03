
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Neon Demon to the database
movies.insert(
    title="The Neon Demon", 
    year=2016, 
    plot="When aspiring model Jesse moves to Los Angeles, her youth and vitality are devoured by a group of beauty-obsessed women who will take any means necessary to get what she has.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Neon Demon", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    