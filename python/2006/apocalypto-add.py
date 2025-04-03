
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Apocalypto to the database
movies.insert(
    title="Apocalypto", 
    year=2006, 
    plot="As the Mayan kingdom faces its decline, the rulers insist the key to prosperity is to build more temples and offer human sacrifices. Jaguar Paw, a young man captured for sacrifice, flees to avoid his fate.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Apocalypto", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    