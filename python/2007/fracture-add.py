
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Fracture to the database
movies.insert(
    title="Fracture", 
    year=2007, 
    plot="An attorney, intent on climbing the career ladder toward success, finds an unlikely opponent in a manipulative criminal he is trying to prosecute.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="Fracture", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    