
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="A Hologram for the King", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="A Hologram for the King", 
        year=2016, 
        plot="A failed American sales rep looks to recoup his losses by traveling to Saudi Arabia and selling his company's product to a wealthy monarch.", 
        rating=6.1
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    