
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Chuck to the database
movies.insert(
    title="Chuck", 
    year=2016, 
    plot="A drama inspired by the life of heavyweight boxer Chuck Wepner.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Chuck", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    