
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Godzilla", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Godzilla", 
        year=2014, 
        plot="The world is beset by the appearance of monstrous creatures, but one of them may be the only one who can save humanity.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    