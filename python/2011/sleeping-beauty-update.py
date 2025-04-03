
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Sleeping Beauty", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Sleeping Beauty", 
        year=2011, 
        plot="A haunting portrait of Lucy, a young university student drawn into a mysterious hidden world of unspoken desires.", 
        rating=5.3
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    