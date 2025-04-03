
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Lavender to the database
movies.insert(
    title="Lavender", 
    year=2016, 
    plot="After losing her memory, a woman begins to see unexplained things after her psychiatrist suggests she visit her childhood home.", 
    rating=5.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Lavender", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    