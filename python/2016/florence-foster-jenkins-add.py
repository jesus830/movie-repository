
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Florence Foster Jenkins to the database
movies.insert(
    title="Florence Foster Jenkins", 
    year=2016, 
    plot="The story of Florence Foster Jenkins, a New York heiress who dreamed of becoming an opera singer, despite having a terrible singing voice.", 
    rating=6.9
)

# Confirm that the movie was added
movie = movies.select(
    title="Florence Foster Jenkins", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    