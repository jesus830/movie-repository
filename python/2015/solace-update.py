
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Solace", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Solace", 
        year=2015, 
        plot="A psychic works with the FBI in order to hunt down a serial killer.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    