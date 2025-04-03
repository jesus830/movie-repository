
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Gravity to the database
movies.insert(
    title="Gravity", 
    year=2013, 
    plot="Two astronauts work together to survive after an accident which leaves them alone in space.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Gravity", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    