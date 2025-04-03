
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Your Highness", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Your Highness", 
        year=2011, 
        plot="When Prince Fabious's bride is kidnapped, he goes on a quest to rescue her... accompanied by his lazy useless brother Thadeous.", 
        rating=5.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    