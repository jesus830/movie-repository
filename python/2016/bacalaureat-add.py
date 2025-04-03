
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Bacalaureat to the database
movies.insert(
    title="Bacalaureat", 
    year=2016, 
    plot="A film about compromises and the implications of the parent's role.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="Bacalaureat", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    