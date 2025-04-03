
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="(500) Days of Summer", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="(500) Days of Summer", 
        year=2009, 
        plot="An offbeat romantic comedy about a woman who doesn't believe true love exists, and the young man who falls for her.", 
        rating=7.7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    