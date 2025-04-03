
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Project X to the database
movies.insert(
    title="Project X", 
    year=2012, 
    plot="3 high school seniors throw a birthday party to make a name for themselves. As the night progresses, things spiral out of control as word of the party spreads.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Project X", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    