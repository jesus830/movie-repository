
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Seventh Son to the database
movies.insert(
    title="Seventh Son", 
    year=2014, 
    plot="When Mother Malkin, the queen of evil witches, escapes the pit she was imprisoned in by professional monster hunter Spook decades ago and kills his apprentice, he recruits young Tom, the seventh son of the seventh son, to help him.", 
    rating=5.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Seventh Son", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    