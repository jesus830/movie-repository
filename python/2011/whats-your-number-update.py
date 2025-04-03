
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="What's Your Number?", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="What's Your Number?", 
        year=2011, 
        plot="A woman looks back at the past nineteen men she's had relationships with in her life and wonders if one of them might be her one true love.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    