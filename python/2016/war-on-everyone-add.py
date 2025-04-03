
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add War on Everyone to the database
movies.insert(
    title="War on Everyone", 
    year=2016, 
    plot="Two corrupt cops set out to blackmail and frame every criminal unfortunate enough to cross their path. Events, however, are complicated by the arrival of someone who appears to be even more dangerous than they are.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="War on Everyone", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    