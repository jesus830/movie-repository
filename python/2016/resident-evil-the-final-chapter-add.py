
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Resident Evil: The Final Chapter to the database
movies.insert(
    title="Resident Evil: The Final Chapter", 
    year=2016, 
    plot="Alice returns to where the nightmare began: The Hive in Raccoon City, where the Umbrella Corporation is gathering its forces for a final strike against the only remaining survivors of the apocalypse.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Resident Evil: The Final Chapter", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    