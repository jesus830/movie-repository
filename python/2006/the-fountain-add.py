
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Fountain to the database
movies.insert(
    title="The Fountain", 
    year=2006, 
    plot="As a modern-day scientist, Tommy is struggling with mortality, desperately searching for the medical breakthrough that will save the life of his cancer-stricken wife, Izzi.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="The Fountain", 
    year=2006
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    