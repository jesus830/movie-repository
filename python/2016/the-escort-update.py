
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="The Escort", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="The Escort", 
        year=2016, 
        plot="Desperate for a good story, a sex-addicted journalist throws himself into the world of high-class escorts when he starts following a Stanford-educated prostitute.", 
        rating=6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    