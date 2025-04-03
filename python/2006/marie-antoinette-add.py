
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Marie Antoinette to the database
movies.insert(
    title="Marie Antoinette", 
    year=2006, 
    plot="The retelling of France's iconic but ill-fated queen, Marie Antoinette. From her betrothal and marriage to Louis XVI at 15 to her reign as queen at 19 and to the end of her reign as queen, and ultimately the fall of Versailles.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Marie Antoinette", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    