
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Secret Life of Pets", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Secret Life of Pets", 
        year=2016, 
        plot="The quiet life of a terrier named Max is upended when his owner takes in Duke, a stray whom Max instantly dislikes.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    