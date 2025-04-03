
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Room", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Room", 
        year=2015, 
        plot="A young boy is raised within the confines of a small shed.", 
        rating=8.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    