
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Monsters University to the database
movies.insert(
    title="Monsters University", 
    year=2013, 
    plot="A look at the relationship between Mike and Sulley during their days at Monsters University -- when they weren't necessarily the best of friends.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Monsters University", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    