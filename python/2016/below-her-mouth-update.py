
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Below Her Mouth", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Below Her Mouth", 
        year=2016, 
        plot="An unexpected affair quickly escalates into a heart-stopping reality for two women whose passionate connection changes their lives forever.", 
        rating=5.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    