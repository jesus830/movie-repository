
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Magnificent Seven", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Magnificent Seven", 
        year=2016, 
        plot="Seven gunmen in the old west gradually come together to help a poor village against savage thieves.", 
        rating=6.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    