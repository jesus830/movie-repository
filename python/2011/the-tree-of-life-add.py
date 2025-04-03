
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Tree of Life to the database
movies.insert(
    title="The Tree of Life", 
    year=2011, 
    plot="The story of a family in Waco, Texas in 1956. The eldest son witnesses the loss of innocence and struggles with his parents' conflicting teachings.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="The Tree of Life", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    