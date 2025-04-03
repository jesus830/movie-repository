
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Winter's Bone to the database
movies.insert(
    title="Winter's Bone", 
    year=2010, 
    plot="An unflinching Ozark Mountain girl hacks through dangerous social terrain as she hunts down her drug-dealing father while trying to keep her family intact.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Winter's Bone", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    