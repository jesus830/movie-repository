
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="2012", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="2012", 
        year=2009, 
        plot="A frustrated writer struggles to keep his family alive when a series of global catastrophes threatens to annihilate mankind.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    