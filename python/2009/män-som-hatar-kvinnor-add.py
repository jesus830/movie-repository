
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Män som hatar kvinnor to the database
movies.insert(
    title="Män som hatar kvinnor", 
    year=2009, 
    plot="A journalist is aided in his search for a woman who has been missing -- or dead -- for forty years by a young female hacker.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Män som hatar kvinnor", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    