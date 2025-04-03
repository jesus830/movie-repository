
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Jupiter Ascending to the database
movies.insert(
    title="Jupiter Ascending", 
    year=2015, 
    plot="A young woman discovers her destiny as an heiress of intergalactic nobility and must fight to protect the inhabitants of Earth from an ancient and destructive industry.", 
    rating=5.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Jupiter Ascending", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    