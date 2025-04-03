
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Good Kids", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Good Kids", 
        year=2016, 
        plot="Four high school students look to redefine themselves after graduation.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    