
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 1408 to the database
movies.insert(
    title="1408", 
    year=2007, 
    plot="A man who specializes in debunking paranormal occurrences checks into the fabled room 1408 in the Dolphin Hotel. Soon after settling in, he confronts genuine terror.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="1408", 
    year=2007
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    