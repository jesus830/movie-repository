
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Hands of Stone to the database
movies.insert(
    title="Hands of Stone", 
    year=2016, 
    plot="The legendary Roberto Duran and his equally legendary trainer Ray Arcel change each other's lives.", 
    rating=6.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Hands of Stone", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    