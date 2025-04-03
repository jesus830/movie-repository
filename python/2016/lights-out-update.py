
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Lights Out", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Lights Out", 
        year=2016, 
        plot="Rebecca must unlock the terror behind her little brother's experiences that once tested her sanity, bringing her face to face with an entity attached to their mother.", 
        rating=6.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    