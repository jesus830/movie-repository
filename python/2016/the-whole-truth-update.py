
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Whole Truth", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Whole Truth", 
        year=2016, 
        plot="A defense attorney works to get his teenage client acquitted of murdering his wealthy father.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    