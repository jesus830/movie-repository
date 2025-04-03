
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="I.T.", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="I.T.", 
        year=2016, 
        plot="A self-proclaimed millionaire, has his life turned upside down after firing his I.T. consultant.", 
        rating=5.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    