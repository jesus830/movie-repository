
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Ghost Writer to the database
movies.insert(
    title="The Ghost Writer", 
    year=2010, 
    plot="A ghostwriter hired to complete the memoirs of a former British prime minister uncovers secrets that put his own life in jeopardy.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Ghost Writer", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    