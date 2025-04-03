
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Mr. Brooks", 
    year=2007
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Mr. Brooks", 
        year=2007, 
        plot="A psychological thriller about a man who is sometimes controlled by his murder-and-mayhem-loving alter ego.", 
        rating=7.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    