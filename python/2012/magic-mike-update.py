
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Magic Mike", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Magic Mike", 
        year=2012, 
        plot="A male stripper teaches a younger performer how to party, pick up women, and make easy money.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    