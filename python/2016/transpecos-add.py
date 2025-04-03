
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Transpecos to the database
movies.insert(
    title="Transpecos", 
    year=2016, 
    plot="For three Border Patrol agents working a remote desert checkpoint, the contents of one car will reveal an insidious plot within their own ranks. The next 24 hours will take them on a treacherous journey that could cost them their lives.", 
    rating=5.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Transpecos", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    