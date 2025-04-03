
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="La tortue rouge", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="La tortue rouge", 
        year=2016, 
        plot="A man is shipwrecked on a deserted island and encounters a red turtle, which changes his life.", 
        rating=7.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    