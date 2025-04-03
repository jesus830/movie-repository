
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Queen of Katwe to the database
movies.insert(
    title="Queen of Katwe", 
    year=2016, 
    plot="A Ugandan girl sees her world rapidly change after being introduced to the game of chess.", 
    rating=7.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Queen of Katwe", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    