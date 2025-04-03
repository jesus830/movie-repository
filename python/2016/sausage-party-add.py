
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sausage Party to the database
movies.insert(
    title="Sausage Party", 
    year=2016, 
    plot="A sausage strives to discover the truth about his existence.", 
    rating=6.3
)

# Confirm that the movie was added
movie = movies.select(
    title="Sausage Party", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    