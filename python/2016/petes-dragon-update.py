
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Pete's Dragon", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Pete's Dragon", 
        year=2016, 
        plot="The adventures of an orphaned boy named Pete and his best friend Elliot, who just so happens to be a dragon.", 
        rating=6.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    