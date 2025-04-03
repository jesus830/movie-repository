
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Pixels", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Pixels", 
        year=2015, 
        plot="When aliens misinterpret video feeds of classic arcade games as a declaration of war, they attack the Earth in the form of the video games.", 
        rating=5.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    