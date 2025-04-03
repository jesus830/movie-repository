
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Final Destination 5", 
    year=2011
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Final Destination 5", 
        year=2011, 
        plot="Survivors of a suspension-bridge collapse learn there's no way you can cheat Death.", 
        rating=5.9
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    