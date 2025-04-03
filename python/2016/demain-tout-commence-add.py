
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Demain tout commence to the database
movies.insert(
    title="Demain tout commence", 
    year=2016, 
    plot="Samuel parties hard in the Marseille area of France and is awoken one morning by a woman carrying a baby she claims is his. She drives off leaving him with a wailing infant; he gives chase ... See full summary »", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Demain tout commence", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    