
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The BFG to the database
movies.insert(
    title="The BFG", 
    year=2016, 
    plot="An orphan little girl befriends a benevolent giant who takes her to Giant Country, where they attempt to stop the man-eating giants that are invading the human world.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="The BFG", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    