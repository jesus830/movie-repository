
from movies import MovieRepository

# Create a new movie repository using the default configuration
movies = MovieRepository()

# Add About Time to the database
movies.insert(
    title="About Time", 
    year=2013, 
    plot="At the age of 21, Tim discovers he can travel in time and change what happens and has happened in his own life. His decision to make his world a better place by getting a girlfriend turns out not to be as easy as you might think.", 
    rating=7.8
)

# Confirm that the movie was added
movie = movies.select(
    title="About Time", 
    year=2013
)
if movie:
    # The movie was found
    print(f"Movie found: {movie}")
else:
    # The movie was not found
    print("Movie not found")
    