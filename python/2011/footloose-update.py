
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Footloose", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Footloose", 
        year=2011, 
        plot="City teenager Ren MacCormack moves to a small town where rock music and dancing have been banned, and his rebellious spirit shakes up the populace.", 
        rating=5.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    