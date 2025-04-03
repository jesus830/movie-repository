
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Guardians of the Galaxy", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Guardians of the Galaxy", 
        year=2014, 
        plot="A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.", 
        rating=8.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    