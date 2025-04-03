
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Birdman or (The Unexpected Virtue of Ignorance)", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Birdman or (The Unexpected Virtue of Ignorance)", 
        year=2014, 
        plot="Illustrated upon the progress of his latest Broadway play, a former popular actor's struggle to cope with his current life as a wasted actor is shown.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    