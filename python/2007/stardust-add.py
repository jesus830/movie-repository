
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Stardust to the database
movies.insert(
    title="Stardust", 
    year=2007, 
    plot="In a countryside town bordering on a magical land, a young man makes a promise to his beloved that he'll retrieve a fallen star by venturing into the magical realm.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Stardust", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    