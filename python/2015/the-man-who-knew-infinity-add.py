
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Man Who Knew Infinity to the database
movies.insert(
    title="The Man Who Knew Infinity", 
    year=2015, 
    plot="The story of the life and academic career of the pioneer Indian mathematician, Srinivasa Ramanujan, and his friendship with his mentor, Professor G.H. Hardy.", 
    rating=7.2
)

# Confirm that the movie was added
movie = movies.select(
    title="The Man Who Knew Infinity", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    