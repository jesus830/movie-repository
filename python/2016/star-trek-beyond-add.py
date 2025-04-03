
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Star Trek Beyond to the database
movies.insert(
    title="Star Trek Beyond", 
    year=2016, 
    plot="The USS Enterprise crew explores the furthest reaches of uncharted space, where they encounter a new ruthless enemy who puts them and everything the Federation stands for to the test.", 
    rating=7.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Star Trek Beyond", 
    year=2016
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    