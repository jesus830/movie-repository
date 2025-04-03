
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Happening to the database
movies.insert(
    title="The Happening", 
    year=2008, 
    plot="A science teacher, his wife, and a young girl struggle to survive a plague that causes those infected to commit suicide.", 
    rating=5
)

# Confirm that the movie was added
movie = movies.select(
    title="The Happening", 
    year=2008
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    