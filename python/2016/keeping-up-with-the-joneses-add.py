
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Keeping Up with the Joneses to the database
movies.insert(
    title="Keeping Up with the Joneses", 
    year=2016, 
    plot="A suburban couple becomes embroiled in an international espionage plot when they discover that their seemingly perfect new neighbors are government spies.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Keeping Up with the Joneses", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    