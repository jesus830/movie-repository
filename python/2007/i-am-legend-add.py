
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add I Am Legend to the database
movies.insert(
    title="I Am Legend", 
    year=2007, 
    plot="Years after a plague kills most of humanity and transforms the rest into monsters, the sole survivor in New York City struggles valiantly to find a cure.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="I Am Legend", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    