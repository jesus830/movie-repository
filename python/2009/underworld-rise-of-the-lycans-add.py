
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Underworld: Rise of the Lycans to the database
movies.insert(
    title="Underworld: Rise of the Lycans", 
    year=2009, 
    plot="An origins story centered on the centuries-old feud between the race of aristocratic vampires and their onetime slaves, the Lycans.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Underworld: Rise of the Lycans", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    