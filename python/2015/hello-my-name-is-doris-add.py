
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hello, My Name Is Doris to the database
movies.insert(
    title="Hello, My Name Is Doris", 
    year=2015, 
    plot="A self-help seminar inspires a sixty-something woman to romantically pursue her younger co-worker.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="Hello, My Name Is Doris", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    