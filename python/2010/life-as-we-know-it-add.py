
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Life as We Know It to the database
movies.insert(
    title="Life as We Know It", 
    year=2010, 
    plot="Two single adults become caregivers to an orphaned girl when their mutual best friends die in an accident.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Life as We Know It", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    