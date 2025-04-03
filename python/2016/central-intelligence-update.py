
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Central Intelligence", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Central Intelligence", 
        year=2016, 
        plot="After he reconnects with an awkward pal from high school through Facebook, a mild-mannered accountant is lured into the world of international espionage.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    