
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Disappointments Room", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Disappointments Room", 
        year=2016, 
        plot="A mother and her young son release unimaginable horrors from the attic of their rural dream home.", 
        rating=3.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    