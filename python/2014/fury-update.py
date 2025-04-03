
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Fury", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Fury", 
        year=2014, 
        plot="A grizzled tank commander makes tough decisions as he and his crew fight their way across Germany in April, 1945.", 
        rating=7.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    