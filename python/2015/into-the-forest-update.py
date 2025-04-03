
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Into the Forest", 
    year=2015
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Into the Forest", 
        year=2015, 
        plot="After a massive power outage, two sisters learn to survive on their own in their isolated woodland home.", 
        rating=5.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    