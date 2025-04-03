
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Alice Through the Looking Glass", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Alice Through the Looking Glass", 
        year=2016, 
        plot="Alice returns to the whimsical world of Wonderland and travels back in time to help the Mad Hatter.", 
        rating=6.2
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    