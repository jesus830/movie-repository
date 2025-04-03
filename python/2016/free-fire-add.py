
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Free Fire to the database
movies.insert(
    title="Free Fire", 
    year=2016, 
    plot="Set in Boston in 1978, a meeting in a deserted warehouse between two gangs turns into a shootout and a game of survival.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Free Fire", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    