
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Sex Tape to the database
movies.insert(
    title="Sex Tape", 
    year=2014, 
    plot="A married couple wake up to discover that the sex tape they made the evening before has gone missing, leading to a frantic search for its whereabouts.", 
    rating=5.1
)

# Confirm that the movie was added
movie = movies.select(
    title="Sex Tape", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    