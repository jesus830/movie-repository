
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pacific Rim to the database
movies.insert(
    title="Pacific Rim", 
    year=2013, 
    plot="As a war between humankind and monstrous sea creatures wages on, a former pilot and a trainee are paired up to drive a seemingly obsolete special weapon in a desperate effort to save the world from the apocalypse.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Pacific Rim", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    