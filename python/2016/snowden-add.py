
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Snowden to the database
movies.insert(
    title="Snowden", 
    year=2016, 
    plot="The NSA's illegal surveillance techniques are leaked to the public by one of the agency's employees, Edward Snowden, in the form of thousands of classified documents distributed to the press.", 
    rating=7.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Snowden", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    