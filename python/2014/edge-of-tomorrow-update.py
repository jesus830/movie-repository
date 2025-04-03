
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Edge of Tomorrow", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Edge of Tomorrow", 
        year=2014, 
        plot="A soldier fighting aliens gets to relive the same day over and over again, the day restarting every time he dies.", 
        rating=7.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    