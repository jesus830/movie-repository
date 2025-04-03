
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Whole Truth to the database
movies.insert(
    title="The Whole Truth", 
    year=2016, 
    plot="A defense attorney works to get his teenage client acquitted of murdering his wealthy father.", 
    rating=6.1
)

# Confirm that the movie was added
movie = movies.select(
    title="The Whole Truth", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    