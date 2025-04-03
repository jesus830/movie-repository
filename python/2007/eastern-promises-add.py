
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Eastern Promises to the database
movies.insert(
    title="Eastern Promises", 
    year=2007, 
    plot="A Russian teenager living in London who dies during childbirth leaves clues to a midwife in her journal that could tie her child to a rape involving a violent Russian mob family.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Eastern Promises", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    