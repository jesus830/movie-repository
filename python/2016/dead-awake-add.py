
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Dead Awake to the database
movies.insert(
    title="Dead Awake", 
    year=2016, 
    plot="A young woman must save herself and her friends from an ancient evil that stalks its victims through the real-life phenomenon of sleep paralysis.", 
    rating=4.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Dead Awake", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    