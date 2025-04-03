
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Amazing Spider-Man to the database
movies.insert(
    title="The Amazing Spider-Man", 
    year=2012, 
    plot="After Peter Parker is bitten by a genetically altered spider, he gains newfound, spider-like powers and ventures out to solve the mystery of his parent's mysterious death.", 
    rating=7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Amazing Spider-Man", 
    year=2012
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    