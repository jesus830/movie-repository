
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Prince of Persia: The Sands of Time to the database
movies.insert(
    title="Prince of Persia: The Sands of Time", 
    year=2010, 
    plot="A young fugitive prince and princess must stop a villain who unknowingly threatens to destroy the world with a special dagger that enables the magic sand inside to reverse time.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Prince of Persia: The Sands of Time", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    