
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Final Girl", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Final Girl", 
        year=2015, 
        plot="A man teaches a young woman how to become a complete weapon. Later she is approached by a group of sadistic teens who kill blonde women for unknown reasons. The hunting season begins.", 
        rating=4.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    