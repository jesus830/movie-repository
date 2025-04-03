
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Warcraft to the database
movies.insert(
    title="Warcraft", 
    year=2016, 
    plot="As an Orc horde invades the planet Azeroth using a magic portal, a few human heroes and dissenting Orcs must attempt to stop the true evil behind this war.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Warcraft", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    