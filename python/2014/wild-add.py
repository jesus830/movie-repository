
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Wild to the database
movies.insert(
    title="Wild", 
    year=2014, 
    plot="A chronicle of one woman's 1,100-mile solo hike undertaken as a way to recover from a recent personal tragedy.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Wild", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    