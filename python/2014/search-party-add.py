
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add Search Party to the database
movies.insert(
    title="Search Party", 
    year=2014, 
    plot="A pair of friends embark on a mission to reunite their pal with the woman he was going to marry.", 
    rating=5.6
)

# Confirm that the movie was added
movie = movies.select(
    title="Search Party", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    