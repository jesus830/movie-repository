
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Final Girl to the database
movies.insert(
    title="Final Girl", 
    year=2015, 
    plot="A man teaches a young woman how to become a complete weapon. Later she is approached by a group of sadistic teens who kill blonde women for unknown reasons. The hunting season begins.", 
    rating=4.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Final Girl", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    