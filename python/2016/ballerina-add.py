
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Ballerina to the database
movies.insert(
    title="Ballerina", 
    year=2016, 
    plot="An orphan girl dreams of becoming a ballerina and flees her rural Brittany for Paris, where she passes for someone else and accedes to the position of pupil at the Grand Opera house.", 
    rating=6.8
)

# Confirm that the movie was added
movie = movies.select(
    title="Ballerina", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    