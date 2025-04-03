
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Prometheus", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Prometheus", 
        year=2012, 
        plot="Following clues to the origin of mankind, a team finds a structure on a distant moon, but they soon realize they are not alone.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    