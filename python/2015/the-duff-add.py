
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The DUFF to the database
movies.insert(
    title="The DUFF", 
    year=2015, 
    plot="A high school senior instigates a social pecking order revolution after finding out that she has been labeled the DUFF - Designated Ugly Fat Friend - by her prettier, more popular counterparts.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="The DUFF", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    