
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Contagion to the database
movies.insert(
    title="Contagion", 
    year=2011, 
    plot="Healthcare professionals, government officials and everyday people find themselves in the midst of a worldwide epidemic as the CDC works to find a cure.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Contagion", 
    year=2011
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    