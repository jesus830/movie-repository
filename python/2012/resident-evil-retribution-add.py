
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Resident Evil: Retribution to the database
movies.insert(
    title="Resident Evil: Retribution", 
    year=2012, 
    plot="Alice fights alongside a resistance movement to regain her freedom from an Umbrella Corporation testing facility.", 
    rating=5.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Resident Evil: Retribution", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    