
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Bourne Legacy to the database
movies.insert(
    title="The Bourne Legacy", 
    year=2012, 
    plot="An expansion of the universe from Robert Ludlum's novels, centered on a new hero whose stakes have been triggered by the events of the previous three films.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Bourne Legacy", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    