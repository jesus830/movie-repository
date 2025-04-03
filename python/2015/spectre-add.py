
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Spectre to the database
movies.insert(
    title="Spectre", 
    year=2015, 
    plot="A cryptic message from Bond's past sends him on a trail to uncover a sinister organization. While M battles political forces to keep the secret service alive, Bond peels back the layers of deceit to reveal the terrible truth behind SPECTRE.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Spectre", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    