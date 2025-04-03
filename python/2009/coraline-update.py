
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Coraline", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Coraline", 
        year=2009, 
        plot="An adventurous girl finds another world that is a strangely idealized version of her frustrating home, but it has sinister secrets.", 
        rating=7.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    