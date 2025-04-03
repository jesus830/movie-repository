
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Captain America: Civil War to the database
movies.insert(
    title="Captain America: Civil War", 
    year=2016, 
    plot="Political interference in the Avengers' activities causes a rift between former allies Captain America and Iron Man.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Captain America: Civil War", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    