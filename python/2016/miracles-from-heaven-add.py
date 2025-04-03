
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Miracles from Heaven to the database
movies.insert(
    title="Miracles from Heaven", 
    year=2016, 
    plot="A young girl suffering from a rare digestive disorder finds herself miraculously cured after surviving a terrible accident.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Miracles from Heaven", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    