
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add There Will Be Blood to the database
movies.insert(
    title="There Will Be Blood", 
    year=2007, 
    plot="A story of family, religion, hatred, oil and madness, focusing on a turn-of-the-century prospector in the early days of the business.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="There Will Be Blood", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    