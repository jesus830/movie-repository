
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add How to Train Your Dragon to the database
movies.insert(
    title="How to Train Your Dragon", 
    year=2010, 
    plot="A hapless young Viking who aspires to hunt dragons becomes the unlikely friend of a young dragon himself, and learns there may be more to the creatures than he assumed.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="How to Train Your Dragon", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    