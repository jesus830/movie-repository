
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 21 to the database
movies.insert(
    title="21", 
    year=2008, 
    plot=""21" is the fact-based story about six MIT students who were trained to become experts in card counting and subsequently took Vegas casinos for millions in winnings.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="21", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    