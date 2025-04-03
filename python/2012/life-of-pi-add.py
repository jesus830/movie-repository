
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Life of Pi to the database
movies.insert(
    title="Life of Pi", 
    year=2012, 
    plot="A young man who survives a disaster at sea is hurtled into an epic journey of adventure and discovery. While cast away, he forms an unexpected connection with another survivor: a fearsome Bengal tiger.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Life of Pi", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    