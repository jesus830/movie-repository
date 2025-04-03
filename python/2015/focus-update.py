
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Focus", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Focus", 
        year=2015, 
        plot="In the midst of veteran con man Nicky's latest scheme, a woman from his past - now an accomplished femme fatale - shows up and throws his plans for a loop.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    