
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Elysium to the database
movies.insert(
    title="Elysium", 
    year=2013, 
    plot="In the year 2154, the very wealthy live on a man-made space station while the rest of the population resides on a ruined Earth. A man takes on a mission that could bring equality to the polarized worlds.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Elysium", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    