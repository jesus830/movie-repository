
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Ben-Hur to the database
movies.insert(
    title="Ben-Hur", 
    year=2016, 
    plot="Judah Ben-Hur, a prince falsely accused of treason by his adopted brother, an officer in the Roman army, returns to his homeland after years at sea to seek revenge, but finds redemption.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Ben-Hur", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    