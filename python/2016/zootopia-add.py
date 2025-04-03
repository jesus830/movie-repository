
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Zootopia to the database
movies.insert(
    title="Zootopia", 
    year=2016, 
    plot="In a city of anthropomorphic animals, a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Zootopia", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    