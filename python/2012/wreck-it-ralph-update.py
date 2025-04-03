
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Wreck-It Ralph", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Wreck-It Ralph", 
        year=2012, 
        plot="A video game villain wants to be a hero and sets out to fulfill his dream, but his quest brings havoc to the whole arcade where he lives.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    