
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add 42 to the database
movies.insert(
    title="42", 
    year=2013, 
    plot="This movie is about Jackie Robinson and his journey to becoming a Brooklyn Dodger and his life during that time.", 
    rating=7.5
)

# Confirm that the movie was added
movie = movies.select(
    title="42", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    