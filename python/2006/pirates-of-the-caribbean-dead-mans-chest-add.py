
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Pirates of the Caribbean: Dead Man's Chest to the database
movies.insert(
    title="Pirates of the Caribbean: Dead Man's Chest", 
    year=2006, 
    plot="Jack Sparrow races to recover the heart of Davy Jones to avoid enslaving his soul to Jones' service, as other friends and foes seek the heart for their own agenda as well.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Pirates of the Caribbean: Dead Man's Chest", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    