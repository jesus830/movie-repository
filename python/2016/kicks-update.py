
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Kicks", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Kicks", 
        year=2016, 
        plot="Brandon is a 15 year old whose dream is a pair of fresh Air Jordans. Soon after he gets his hands on them, they're stolen by a local hood, causing Brandon and his two friends to go on a dangerous mission through Oakland to retrieve them.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    