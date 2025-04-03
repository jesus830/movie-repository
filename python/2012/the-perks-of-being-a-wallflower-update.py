
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Perks of Being a Wallflower", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Perks of Being a Wallflower", 
        year=2012, 
        plot="An introvert freshman is taken under the wings of two seniors who welcome him to the real world.", 
        rating=8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    