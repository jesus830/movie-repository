
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Max to the database
movies.insert(
    title="Max", 
    year=2015, 
    plot="A Malinois dog that helped American Marines in Afghanistan returns to the United States and is adopted by his handler's family after suffering a traumatic experience.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Max", 
    year=2015
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    