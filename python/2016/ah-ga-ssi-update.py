
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Ah-ga-ssi", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Ah-ga-ssi", 
        year=2016, 
        plot="A woman is hired as a handmaiden to a Japanese heiress, but secretly she is involved in a plot to defraud her.", 
        rating=8.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    