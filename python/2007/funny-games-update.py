
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Funny Games", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Funny Games", 
        year=2007, 
        plot="Two psychopathic young men take a family hostage in their cabin.", 
        rating=6.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    