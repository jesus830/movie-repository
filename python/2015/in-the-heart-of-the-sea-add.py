
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add In the Heart of the Sea to the database
movies.insert(
    title="In the Heart of the Sea", 
    year=2015, 
    plot="A recounting of a New England whaling ship's sinking by a giant whale in 1820, an experience that later inspired the great novel Moby-Dick.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="In the Heart of the Sea", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    