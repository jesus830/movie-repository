
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Trust", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Trust", 
        year=2010, 
        plot="A teenage girl is targeted by an online sexual predator.", 
        rating=7
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    