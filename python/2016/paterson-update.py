
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Paterson", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Paterson", 
        year=2016, 
        plot="A quiet observation of the triumphs and defeats of daily life, along with the poetry evident in its smallest details.", 
        rating=7.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    