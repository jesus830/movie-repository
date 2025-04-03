
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Resident Evil: Retribution", 
    year=2012
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Resident Evil: Retribution", 
        year=2012, 
        plot="Alice fights alongside a resistance movement to regain her freedom from an Umbrella Corporation testing facility.", 
        rating=5.4
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    