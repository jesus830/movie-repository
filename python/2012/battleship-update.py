
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Battleship", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Battleship", 
        year=2012, 
        plot="A fleet of ships is forced to do battle with an armada of unknown origins in order to discover and thwart their destructive goals.", 
        rating=5.8
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    