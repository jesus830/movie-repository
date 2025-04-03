
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Endless Love to the database
movies.insert(
    title="Endless Love", 
    year=2014, 
    plot="The story of a privileged girl and a charismatic boy whose instant desire sparks a love affair made only more reckless by parents trying to keep them apart.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Endless Love", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    