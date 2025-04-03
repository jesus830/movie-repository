
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Room to the database
movies.insert(
    title="Room", 
    year=2015, 
    plot="A young boy is raised within the confines of a small shed.", 
    rating=8.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Room", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    