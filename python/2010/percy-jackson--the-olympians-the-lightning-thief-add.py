
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Percy Jackson & the Olympians: The Lightning Thief to the database
movies.insert(
    title="Percy Jackson & the Olympians: The Lightning Thief", 
    year=2010, 
    plot="A teenager discovers he's the descendant of a Greek god and sets out on an adventure to settle an on-going battle between the gods.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Percy Jackson & the Olympians: The Lightning Thief", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    