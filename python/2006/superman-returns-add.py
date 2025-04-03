
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Superman Returns to the database
movies.insert(
    title="Superman Returns", 
    year=2006, 
    plot="Superman reappears after a long absence, but is challenged by an old foe who uses Kryptonian technology for world domination.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Superman Returns", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    