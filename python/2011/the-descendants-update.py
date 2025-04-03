
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Descendants", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Descendants", 
        year=2011, 
        plot="A land baron tries to reconnect with his two daughters after his wife is seriously injured in a boating accident.", 
        rating=7.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    