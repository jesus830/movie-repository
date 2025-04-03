
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Don't Breathe to the database
movies.insert(
    title="Don't Breathe", 
    year=2016, 
    plot="Hoping to walk away with a massive fortune, a trio of thieves break into the house of a blind man who isn't as helpless as he seems.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Don't Breathe", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    