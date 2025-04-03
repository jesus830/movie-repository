
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Fast Five", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Fast Five", 
        year=2011, 
        plot="Dominic Toretto and his crew of street racers plan a massive heist to buy their freedom while in the sights of a powerful Brazilian drug lord and a dangerous federal agent.", 
        rating=7.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    