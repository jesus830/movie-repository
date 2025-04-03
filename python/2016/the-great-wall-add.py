
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Great Wall to the database
movies.insert(
    title="The Great Wall", 
    year=2016, 
    plot="European mercenaries searching for black powder become embroiled in the defense of the Great Wall of China against a horde of monstrous creatures.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Great Wall", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    