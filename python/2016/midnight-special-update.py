
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Midnight Special", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Midnight Special", 
        year=2016, 
        plot="A father and son go on the run, pursued by the government and a cult drawn to the child's special powers.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    