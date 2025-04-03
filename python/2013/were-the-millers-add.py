
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add We're the Millers to the database
movies.insert(
    title="We're the Millers", 
    year=2013, 
    plot="A veteran pot dealer creates a fake family as part of his plan to move a huge shipment of weed into the U.S. from Mexico.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="We're the Millers", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    