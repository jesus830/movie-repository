
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Independence Day: Resurgence", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Independence Day: Resurgence", 
        year=2016, 
        plot="Two decades after the first Independence Day invasion, Earth is faced with a new extra-Solar threat. But will mankind's new space defenses be enough?", 
        rating=5.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    