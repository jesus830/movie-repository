
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Alice Through the Looking Glass to the database
movies.insert(
    title="Alice Through the Looking Glass", 
    year=2016, 
    plot="Alice returns to the whimsical world of Wonderland and travels back in time to help the Mad Hatter.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Alice Through the Looking Glass", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    