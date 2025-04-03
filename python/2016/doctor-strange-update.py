
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Doctor Strange", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Doctor Strange", 
        year=2016, 
        plot="While on a journey of physical and spiritual healing, a brilliant neurosurgeon is drawn into the world of the mystic arts.", 
        rating=7.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    