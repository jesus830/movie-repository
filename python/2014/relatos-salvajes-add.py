
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Relatos salvajes to the database
movies.insert(
    title="Relatos salvajes", 
    year=2014, 
    plot="Six short stories that explore the extremities of human behavior involving people in distress.", 
    rating=8.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Relatos salvajes", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    