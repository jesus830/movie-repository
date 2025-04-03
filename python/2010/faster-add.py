
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Faster to the database
movies.insert(
    title="Faster", 
    year=2010, 
    plot="An ex-con gets on a series of apparently unrelated killings. He gets tracked by a veteran cop with secrets of his own and an egocentric hit man.", 
    rating=6.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Faster", 
    year=2010
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    