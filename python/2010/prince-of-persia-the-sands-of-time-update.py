
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Prince of Persia: The Sands of Time", 
    year=2010
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Prince of Persia: The Sands of Time", 
        year=2010, 
        plot="A young fugitive prince and princess must stop a villain who unknowingly threatens to destroy the world with a special dagger that enables the magic sand inside to reverse time.", 
        rating=6.6
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    