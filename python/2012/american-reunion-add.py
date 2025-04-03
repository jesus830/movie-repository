
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add American Reunion to the database
movies.insert(
    title="American Reunion", 
    year=2012, 
    plot="Jim, Michelle, Stifler, and their friends reunite in East Great Falls, Michigan for their high school reunion.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="American Reunion", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    