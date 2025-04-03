
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Blended to the database
movies.insert(
    title="Blended", 
    year=2014, 
    plot="After a bad blind date, a man and woman find themselves stuck together at a resort for families, where their attraction grows as their respective kids benefit from the burgeoning relationship.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Blended", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    