
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Hush", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Hush", 
        year=2016, 
        plot="A deaf writer who retreated into the woods to live a solitary life must fight for her life in silence when a masked killer appears at her window.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    