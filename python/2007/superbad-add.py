
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Superbad to the database
movies.insert(
    title="Superbad", 
    year=2007, 
    plot="Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Superbad", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    