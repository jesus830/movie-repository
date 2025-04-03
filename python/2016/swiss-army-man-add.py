
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Swiss Army Man to the database
movies.insert(
    title="Swiss Army Man", 
    year=2016, 
    plot="A hopeless man stranded on a deserted island befriends a dead body and together they go on a surreal journey to get home.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Swiss Army Man", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    