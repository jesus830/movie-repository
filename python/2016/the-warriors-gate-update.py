
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Warriors Gate", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Warriors Gate", 
        year=2016, 
        plot="A teenager is magically transported to China and learns to convert his video game skills into those of a Kung Fu warrior.", 
        rating=5.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    