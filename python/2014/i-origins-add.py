
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add I Origins to the database
movies.insert(
    title="I Origins", 
    year=2014, 
    plot="A molecular biologist and his laboratory partner uncover evidence that may fundamentally change society as we know it.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="I Origins", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    