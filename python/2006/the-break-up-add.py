
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Break-Up to the database
movies.insert(
    title="The Break-Up", 
    year=2006, 
    plot="In a bid to keep their luxurious condo from their significant other, a couple's break-up proceeds to get uglier and nastier by the moment.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Break-Up", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    