
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Legend", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Legend", 
        year=2015, 
        plot="Identical twin gangsters Ronald and Reginald Kray terrorize London during the 1960s.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    