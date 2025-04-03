
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Shin Gojira", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Shin Gojira", 
        year=2016, 
        plot="Japan is plunged into chaos upon the appearance of a giant monster.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    