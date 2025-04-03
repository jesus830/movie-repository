
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="10 Cloverfield Lane", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="10 Cloverfield Lane", 
        year=2016, 
        plot="After getting in a car accident, a woman is held in a shelter with two men, who claim the outside world is affected by a widespread chemical attack.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    