
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Christine to the database
movies.insert(
    title="Christine", 
    year=2016, 
    plot="The story of Christine Chubbuck, a 1970s TV reporter struggling with depression and professional frustrations as she tries to advance her career.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="Christine", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    