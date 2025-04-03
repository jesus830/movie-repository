
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Founder to the database
movies.insert(
    title="The Founder", 
    year=2016, 
    plot="The story of Ray Kroc, a salesman who turned two brothers' innovative fast food eatery, McDonald's, into one of the biggest restaurant businesses in the world with a combination of ambition, persistence, and ruthlessness.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Founder", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    