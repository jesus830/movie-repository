
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Knight of Cups to the database
movies.insert(
    title="Knight of Cups", 
    year=2015, 
    plot="A writer indulging in all that Los Angeles and Las Vegas has to offer undertakes a search for love and self via a series of adventures with six different women.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Knight of Cups", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    