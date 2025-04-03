
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Rescue Dawn", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Rescue Dawn", 
        year=2006, 
        plot="A U.S. fighter pilot's epic struggle of survival after being shot down on a mission over Laos during the Vietnam War.", 
        rating=7.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    