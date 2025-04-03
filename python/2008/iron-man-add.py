
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Iron Man to the database
movies.insert(
    title="Iron Man", 
    year=2008, 
    plot="After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Iron Man", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    