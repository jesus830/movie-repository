
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Invitation", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Invitation", 
        year=2015, 
        plot="While attending a dinner party at his former home, a man thinks his ex-wife and her new husband have sinister intentions for their guests.", 
        rating=6.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    