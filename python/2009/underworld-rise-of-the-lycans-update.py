
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Underworld: Rise of the Lycans", 
    year=2009
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Underworld: Rise of the Lycans", 
        year=2009, 
        plot="An origins story centered on the centuries-old feud between the race of aristocratic vampires and their onetime slaves, the Lycans.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    