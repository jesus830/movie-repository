
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Final Destination 5 to the database
movies.insert(
    title="Final Destination 5", 
    year=2011, 
    plot="Survivors of a suspension-bridge collapse learn there's no way you can cheat Death.", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Final Destination 5", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    