
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Mean Dreams to the database
movies.insert(
    title="Mean Dreams", 
    year=2016, 
    plot="Follows Casey and Jonas, two teenagers desperate to escape their broken and abusive homes and examines the desperation of life on the run and the beauty of first love.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Mean Dreams", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    