
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Neighbor to the database
movies.insert(
    title="The Neighbor", 
    year=2016, 
    plot="Set in Cutter Mississippi, the film follows a man who discovers the dark truth about his neighbor and the secrets he may be keeping in the cellar.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Neighbor", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    