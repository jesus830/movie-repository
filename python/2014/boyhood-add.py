
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Boyhood to the database
movies.insert(
    title="Boyhood", 
    year=2014, 
    plot="The life of Mason, from early childhood to his arrival at college.", 
    rating=7.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Boyhood", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    