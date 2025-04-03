
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Clash of the Titans to the database
movies.insert(
    title="Clash of the Titans", 
    year=2010, 
    plot="Perseus demigod, son of Zeus, battles the minions of the underworld to stop them from conquering heaven and earth.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Clash of the Titans", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    