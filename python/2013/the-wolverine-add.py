
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Wolverine to the database
movies.insert(
    title="The Wolverine", 
    year=2013, 
    plot="When Wolverine is summoned to Japan by an old acquaintance, he is embroiled in a conflict that forces him to confront his own demons.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Wolverine", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    