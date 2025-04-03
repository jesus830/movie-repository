
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Orphan to the database
movies.insert(
    title="Orphan", 
    year=2009, 
    plot="A husband and wife who recently lost their baby adopt a nine year-old girl who is not nearly as innocent as she claims to be.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Orphan", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    