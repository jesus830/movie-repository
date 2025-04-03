
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Fallen to the database
movies.insert(
    title="Fallen", 
    year=2016, 
    plot="A young girl finds herself in a reform school after therapy since she was blamed for the death of a young boy. At the school she finds herself drawn to a fellow student, unaware that he is an angel, and has loved her for thousands of years.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Fallen", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    