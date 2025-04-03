
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 3 Days to Kill to the database
movies.insert(
    title="3 Days to Kill", 
    year=2014, 
    plot="A dying CIA agent trying to reconnect with his estranged daughter is offered an experimental drug that could save his life in exchange for one last assignment.", 
    rating=6.2
)

# Confirm that the movie was added
movie = movies.select(
    title="3 Days to Kill", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    