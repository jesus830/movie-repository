
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Invitation to the database
movies.insert(
    title="The Invitation", 
    year=2015, 
    plot="While attending a dinner party at his former home, a man thinks his ex-wife and her new husband have sinister intentions for their guests.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Invitation", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    