
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Resident Evil: The Final Chapter", 
    year=2016
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Resident Evil: The Final Chapter", 
        year=2016, 
        plot="Alice returns to where the nightmare began: The Hive in Raccoon City, where the Umbrella Corporation is gathering its forces for a final strike against the only remaining survivors of the apocalypse.", 
        rating=5.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    