
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Raw (II) to the database
movies.insert(
    title="Raw (II)", 
    year=2016, 
    plot="When a young vegetarian undergoes a carnivorous hazing ritual at vet school, an unbidden taste for meat begins to grow in her.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Raw (II)", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    