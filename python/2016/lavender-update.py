
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Lavender", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Lavender", 
        year=2016, 
        plot="After losing her memory, a woman begins to see unexplained things after her psychiatrist suggests she visit her childhood home.", 
        rating=5.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    