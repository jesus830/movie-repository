
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Brave to the database
movies.insert(
    title="Brave", 
    year=2012, 
    plot="Determined to make her own path in life, Princess Merida defies a custom that brings chaos to her kingdom. Granted one wish, Merida must rely on her bravery and her archery skills to undo a beastly curse.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Brave", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    