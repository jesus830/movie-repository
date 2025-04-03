
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Wolves at the Door to the database
movies.insert(
    title="Wolves at the Door", 
    year=2016, 
    plot="Four friends gather at an elegant home during the Summer of Love, 1969. Unbeknownst to them, deadly visitors are waiting outside. What begins as a simple farewell party turns to a night of ... See full summary »", 
    rating=4.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Wolves at the Door", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    