
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Realive to the database
movies.insert(
    title="Realive", 
    year=2016, 
    plot="Marc (Tom Hughes) is diagnosed with a disease and is given one year left to live. Unable to accept his own end, he decides to freeze his body. Sixty years later, in the year 2084, he ... See full summary »", 
    rating=5.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Realive", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    