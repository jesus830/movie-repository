
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Deadpool to the database
movies.insert(
    title="Deadpool", 
    year=2016, 
    plot="A fast-talking mercenary with a morbid sense of humor is subjected to a rogue experiment that leaves him with accelerated healing powers and a quest for revenge.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="Deadpool", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    