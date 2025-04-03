
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Hail, Caesar!", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Hail, Caesar!", 
        year=2016, 
        plot="A Hollywood fixer in the 1950s works to keep the studio's stars in line.", 
        rating=6.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    