
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Kubo and the Two Strings to the database
movies.insert(
    title="Kubo and the Two Strings", 
    year=2016, 
    plot="A young boy named Kubo must locate a magical suit of armour worn by his late father in order to defeat a vengeful spirit from the past.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Kubo and the Two Strings", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    