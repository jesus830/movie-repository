
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Purge to the database
movies.insert(
    title="The Purge", 
    year=2013, 
    plot="A wealthy family are held hostage for harboring the target of a murderous syndicate during the Purge, a 12-hour period in which any and all crime is legal.", 
    rating=5.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Purge", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    