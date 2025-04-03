
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Adjustment Bureau", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Adjustment Bureau", 
        year=2011, 
        plot="The affair between a politician and a contemporary dancer is affected by mysterious forces keeping the lovers apart.", 
        rating=7.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    