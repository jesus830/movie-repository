
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Percy Jackson & the Olympians: The Lightning Thief", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Percy Jackson & the Olympians: The Lightning Thief", 
        year=2010, 
        plot="A teenager discovers he's the descendant of a Greek god and sets out on an adventure to settle an on-going battle between the gods.", 
        rating=5.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    