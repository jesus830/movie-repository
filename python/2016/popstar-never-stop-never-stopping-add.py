
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Popstar: Never Stop Never Stopping to the database
movies.insert(
    title="Popstar: Never Stop Never Stopping", 
    year=2016, 
    plot="When it becomes clear that his solo album is a failure, a former boy band member does everything in his power to maintain his celebrity status.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Popstar: Never Stop Never Stopping", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    