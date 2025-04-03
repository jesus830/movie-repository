
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Illusionist to the database
movies.insert(
    title="The Illusionist", 
    year=2006, 
    plot="In turn-of-the-century Vienna, a magician uses his abilities to secure the love of a woman far above his social standing.", 
    rating=7.6
)

# Confirm that the movie was added
movie = movies.select(
    title="The Illusionist", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    