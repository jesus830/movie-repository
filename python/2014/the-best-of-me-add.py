
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add The Best of Me to the database
movies.insert(
    title="The Best of Me", 
    year=2014, 
    plot="A pair of former high school sweethearts reunite after many years when they return to visit their small hometown.", 
    rating=6.7
)

# Confirm that the movie was added
movie = movies.select(
    title="The Best of Me", 
    year=2014
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    