
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Coraline to the database
movies.insert(
    title="Coraline", 
    year=2009, 
    plot="An adventurous girl finds another world that is a strangely idealized version of her frustrating home, but it has sinister secrets.", 
    rating=7.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Coraline", 
    year=2009
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    