
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Strangers", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Strangers", 
        year=2008, 
        plot="A young couple staying in an isolated vacation home are terrorized by three unknown assailants.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    