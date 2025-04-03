
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 2307: Winter's Dream to the database
movies.insert(
    title="2307: Winter's Dream", 
    year=2016, 
    plot="In 2307, a future soldier is sent on a mission to hunt down the leader of the humanoid rebellion.", 
    rating=4
)

# Confirm that the movie was added
movie = movies.select(
    title="2307: Winter's Dream", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    