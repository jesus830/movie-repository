
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hugo to the database
movies.insert(
    title="Hugo", 
    year=2011, 
    plot="In Paris in 1931, an orphan named Hugo Cabret who lives in the walls of a train station is wrapped up in a mystery involving his late father and an automaton.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Hugo", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    