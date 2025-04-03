
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Break-Up", 
    year=2006
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Break-Up", 
        year=2006, 
        plot="In a bid to keep their luxurious condo from their significant other, a couple's break-up proceeds to get uglier and nastier by the moment.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    