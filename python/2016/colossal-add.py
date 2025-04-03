
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Colossal to the database
movies.insert(
    title="Colossal", 
    year=2016, 
    plot="Gloria is an out-of-work party girl forced to leave her life in New York City, and move back home. When reports surface that a giant creature is destroying Seoul, she gradually comes to the realization that she is somehow connected to this phenomenon.", 
    rating=6.4
)

# Confirm that the movie was added
movie = movies.select(
    title="Colossal", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    