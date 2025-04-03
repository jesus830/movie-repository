
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Lída Baarová", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Lída Baarová", 
        year=2016, 
        plot="A film about the black-and-white era actress Lída Baarová and her doomed love affair.", 
        rating=5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    