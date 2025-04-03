
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="August Rush", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="August Rush", 
        year=2007, 
        plot="A drama with fairy tale elements, where an orphaned musical prodigy uses his gift as a clue to finding his birth parents.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    