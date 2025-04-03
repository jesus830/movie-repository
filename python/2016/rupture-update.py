
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Rupture", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Rupture", 
        year=2016, 
        plot="A single mom tries to break free from a mysterious organization that has abducted her.", 
        rating=4.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    