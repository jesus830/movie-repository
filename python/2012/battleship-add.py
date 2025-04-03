
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Battleship to the database
movies.insert(
    title="Battleship", 
    year=2012, 
    plot="A fleet of ships is forced to do battle with an armada of unknown origins in order to discover and thwart their destructive goals.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Battleship", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    