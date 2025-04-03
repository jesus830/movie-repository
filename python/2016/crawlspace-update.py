
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Crawlspace", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Crawlspace", 
        year=2016, 
        plot="A thriller centered around a widower who moves into a seemingly perfect new home with his daughter and new wife.", 
        rating=5.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    