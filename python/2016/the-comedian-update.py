
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Comedian", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Comedian", 
        year=2016, 
        plot="A look at the life of an aging insult comic named Jack Burke.", 
        rating=5.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    