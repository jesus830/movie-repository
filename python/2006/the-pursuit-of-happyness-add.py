
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Pursuit of Happyness to the database
movies.insert(
    title="The Pursuit of Happyness", 
    year=2006, 
    plot="A struggling salesman takes custody of his son as he's poised to begin a life-changing professional career.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Pursuit of Happyness", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    