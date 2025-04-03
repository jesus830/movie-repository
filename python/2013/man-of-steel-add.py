
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Man of Steel to the database
movies.insert(
    title="Man of Steel", 
    year=2013, 
    plot="Clark Kent, one of the last of an extinguished race disguised as an unremarkable human, is forced to reveal his identity when Earth is invaded by an army of survivors who threaten to bring the planet to the brink of destruction.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Man of Steel", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    