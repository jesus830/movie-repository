
from movies import MovieRepository

# Create a new Movies repository using the default configuration
movies = MovieRepository()

# Confirm that the movie was added
movie = movies.select(
    title="Seventh Son", 
    year=2014
)

if movie:
    # The movie was found, so update it
    movies.update(
        title="Seventh Son", 
        year=2014, 
        plot="When Mother Malkin, the queen of evil witches, escapes the pit she was imprisoned in by professional monster hunter Spook decades ago and kills his apprentice, he recruits young Tom, the seventh son of the seventh son, to help him.", 
        rating=5.5
    )
    print("Movie updated")
else:
    # The movie was not found, so we cannot update
    print("Movie not found")
    