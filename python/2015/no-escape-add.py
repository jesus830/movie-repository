
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add No Escape to the database
movies.insert(
    title="No Escape", 
    year=2015, 
    plot="In their new overseas home, an American family soon finds themselves caught in the middle of a coup, and they frantically look for a safe escape from an environment where foreigners are being immediately executed.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="No Escape", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    