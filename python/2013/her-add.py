
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Her to the database
movies.insert(
    title="Her", 
    year=2013, 
    plot="A lonely writer develops an unlikely relationship with an operating system designed to meet his every need.", 
    rating=8
)

# Confirm that the movie was added
movie = movies.select(
    title="Her", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    