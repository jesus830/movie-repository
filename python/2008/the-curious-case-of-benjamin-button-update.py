
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Curious Case of Benjamin Button", 
    year=2008
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Curious Case of Benjamin Button", 
        year=2008, 
        plot="Tells the story of Benjamin Button, a man who starts aging backwards with bizarre consequences.", 
        rating=7.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    