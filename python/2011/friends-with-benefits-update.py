
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Friends with Benefits", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Friends with Benefits", 
        year=2011, 
        plot="A young man and woman decide to take their friendship to the next level without becoming a couple, but soon discover that adding sex only leads to complications.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    