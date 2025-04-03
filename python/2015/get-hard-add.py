
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Get Hard to the database
movies.insert(
    title="Get Hard", 
    year=2015, 
    plot="When millionaire James King is jailed for fraud and bound for San Quentin, he turns to Darnell Lewis to prep him to go behind bars.", 
    rating=6
)

# Confirm that the movie was added
movie = movies.select(
    title="Get Hard", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    