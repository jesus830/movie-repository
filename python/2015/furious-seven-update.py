
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Furious Seven", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Furious Seven", 
        year=2015, 
        plot="Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother.", 
        rating=7.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    