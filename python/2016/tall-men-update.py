
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Tall Men", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Tall Men", 
        year=2016, 
        plot="A challenged man is stalked by tall phantoms in business suits after he purchases a car with a mysterious black credit card.", 
        rating=3.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    