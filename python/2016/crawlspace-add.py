
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Crawlspace to the database
movies.insert(
    title="Crawlspace", 
    year=2016, 
    plot="A thriller centered around a widower who moves into a seemingly perfect new home with his daughter and new wife.", 
    rating=5.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Crawlspace", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    